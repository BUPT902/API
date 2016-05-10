#coding=utf-8
from django.shortcuts import render
from kong_admin.models import APIReference, ParameterReference, HeaderReference, ErrorReference, ConsumerReference, KeyAuthReference,\
    PluginConfigurationReference
from django.shortcuts import render_to_response,  HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from kong_admin.views import synchronize_api_reference, synchronize_api_references, synchronize_consumer_reference, \
    synchronize_consumer_references
import json
from django import forms
from django.forms import formset_factory, inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from .forms import *
from kong_admin.enums import Plugins


# Create your views here.
def index(request):
    #blog_list = BlogsPost.objects.all()
    response = render_to_response('apiIndex.html')
    response.set_cookie("username", 'test')
    return response


def apiList(request):
    api_list = APIReference.objects.all()
    for api in api_list:
        print(api.API_description)
    context = {
        'api_list' : api_list,
    }
    return render_to_response('apiList.html', context)


def apiCategory(request, param1):
    print(param1)
    api_list = APIReference.objects.filter(APIService_category__exact=param1)
    context = {
        'api_list' : api_list,
    }
    return render_to_response('apiList.html', context)


def apiDetail(request, param1):
    api = APIReference.objects.get(name = param1)
    username = request.COOKIES.get('username', '')
    person = ConsumerReference.objects.get(username = username)
    api_key = person.keyauthreference_related.all()[:1]
    api_key = api_key[0]
    gateway_url = 'http://10.33.6.199:8000'
    url_Parameters = ParameterReference.objects.filter(api__name__exact = param1)
    Headers = HeaderReference.objects.filter(api__name__exact = param1)
    Errors  = ErrorReference.objects.filter(api__name__exact = param1)
    url_example = ""
    for para in url_Parameters:
        url_example += '?' + para.name + '=' + para.defaultValue
    context = {
        'api' : api,
        'gateway_url' : gateway_url,
        'url_Parameters' : url_Parameters,
        'url_example' : url_example,
        'Headers' : Headers,
        'Errors' : Errors,
        'api_key': api_key,
    }
    return render_to_response('apiDetail.html', context)


def userCenter(request):
    username = request.COOKIES.get('username', '')
    person = ConsumerReference.objects.get(username = username)
    apis = person.infos.all()
    buy_apis = person.Buy_consumer.all()
    # for i in buy_apis:
    #     print(i.api)
    context = {
        'my_apis':apis,
        'buy_apis':buy_apis,
    }
    return render_to_response('userCenter.html', context)


def ConfigPlugin(API):
    PluginConfigurationReference.objects.filter(api=API).delete()
    if API.APISecLimit or API.APIDayLimit:
        rate_limit={}
        if API.APISecLimit:
            rate_limit['second'] = API.APISecLimit
        if API.APIDayLimit:
            rate_limit['day'] = API.APIDayLimit
        obj = json.dumps(rate_limit)
        plugin = PluginConfigurationReference(api=API, plugin=Plugins.RATE_LIMITING, config=obj)
        plugin.save()
    plugin = PluginConfigurationReference(api=API, plugin=Plugins.KEY_AUTHENTICATION, config=json.dumps({}))
    plugin.save()
    acl = {}
    acl['whitelist'] = API.name
    plugin = PluginConfigurationReference(api=API, plugin=Plugins.ACL, config=json.dumps(acl))
    plugin.save()


def ConfigPara(API, parameter):
    ParameterReference.objects.filter(api=API).delete()
    ErrorReference.objects.filter(api=API).delete()
    HeaderReference.objects.filter(api=API).delete()
    json_dict = json.loads(parameter)
    errorCode  = json_dict['errorCode']
    header  =  json_dict['header']
    param = json_dict['param']
    for i in errorCode:
        error = ErrorReference(api=API, code=_(errorCode[i]['message']), message=_(errorCode[i]['name']), description=_(errorCode[i]['description']))
        error.save()
    for i in header:
        head = HeaderReference(api=API, name=header[i]['name'], type=header[i]['type'], defaultValue=header[i]['defaultValue'], \
                               description=header[i]['description'], nessesary=header[i]['nessesary'])
        head.save()
    for i in param:
        para = ParameterReference(api=API, name=param[i]['name'], type=param[i]['type'], defaultValue=param[i]['defaultValue'], \
                                  description=param[i]['description'], nessesary=param[i]['nessesary'])
        para.save()
    print(dict)


def registerApi(request):
    if request.method == "POST":
        info = request.POST.copy()
        parameter = info['parameter']
        del info['parameter']
        form = APIForm(info, request.FILES)
        if form.is_valid():
            username = request.COOKIES.get('username', '')
            API_new = form.save(commit=False)
            API_new.request_path = '/' + API_new.name
            API_new.strip_request_path = True
            API_new.owner = ConsumerReference.objects.get(username = username)
            API_new.save()
            ConfigPara(API_new, parameter)
            ConfigPlugin(API_new)
            return HttpResponseRedirect('/userCenter')
        else:
            context = {
                'form': form,
            }
    else:
        form = APIForm()
        context = {
            'form':form,
        }
    return render_to_response('registerApi.html', context=context)


def edit_api(request):
    if request.method == "POST":
        dict = request.POST.dict()
        print(dict['apiName'])
        api = APIReference.objects.get(name=dict['apiName'])
        json_dict = {}
        error_dict = {}
        for i, error in enumerate(ErrorReference.objects.filter(api=api).values()):
            error_dict['err' + str(i)] = error
        json_dict['error'] = error_dict
        param_dict = {}
        for i, param in enumerate(ParameterReference.objects.filter(api=api).values()):
            param_dict['param' + str(i)] = param
        json_dict['param'] = param_dict
        head_dict = {}
        for i, head in enumerate(HeaderReference.objects.filter(api=api).values()):
            head_dict['head' + str(i)] = head
        json_dict['head'] = param_dict
        print(json.dumps(json_dict))
        return HttpResponse(json.dumps(json_dict))



def modifyApi(request, param1):
    print(param1)
    api = APIReference.objects.get(name=param1)
    if request.method == "POST":
        info = request.POST.copy()
        parameter = info['parameter']
        print(parameter)
        del info['parameter']
        form = APIForm_modify(info, request.FILES, instance=api)
        if form.is_valid():
            username = request.COOKIES.get('username', '')
            API_new = form.save(commit=False)
            API_new.save()
            ConfigPara(API_new, parameter)
            ConfigPlugin(API_new)
            return HttpResponseRedirect('/userCenter')
        else:
            context = {
                'form': form,
            }
    else:
        form = APIForm_modify(instance=api)
        context = {
            'form': form,
        }
    return render_to_response('registerApi.html', context=context)



def delete_api(request):
    if request.method == "POST":
        dict = request.POST.dict()
        print(dict['apiName'])
        api = APIReference.objects.get(name=dict['apiName'])
        print(api)
        api.delete()
        return HttpResponseRedirect('/userCenter/')


def ConfigConsumer(username):
    consumer = ConsumerReference(username=username)
    consumer.save()
    KeyAuth = KeyAuthReference(consumer=consumer)
    KeyAuth.save()


def registerConsumer(request):
    if request.method == "GET":
        print(request.GET)
        name = request.GET.get('name')
        back = request.GET.get('callback')
        print(back)
        print(type(name))
        d = {}
        d[name] = '1'
        obj = json.dumps(d)
        print(type(str(back+'('+ obj+')')))
        ConfigConsumer()
        return HttpResponse(str(back+'('+ obj+')'))

def apiHandler(request):
    pass

def apiFooter(request):
    return render_to_response('model/apiFooter.html')


def apiHeader(request):
    return render_to_response('model/apiHeader.html')