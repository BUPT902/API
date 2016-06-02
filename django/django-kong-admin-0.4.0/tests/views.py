#coding=utf-8
from django.shortcuts import render
from kong_admin.models import APIReference, ParameterReference, HeaderReference, ErrorReference, ConsumerReference, KeyAuthReference,\
    PluginConfigurationReference,  BuyReference,  AclReference, Userinfo
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
from kong_admin import factory, logic
from django.core.mail import send_mail
from django.forms import model_to_dict
from requests import get
from django.contrib.auth.models import User

def get_username(request):
    # username = request.session.get('username')
    # if username:
    # username = request.COOKIES.get('username', '')
    #     return username
    # else:
    #     return None
    return 'test'


def login(requst):
    info = requst.POST
    json_obj = json.loads(info['params'])
    if json_obj['status'] == 1:
        requst.session['username'] = json_obj['username']
    obj = json.dumps({'isLog':'1'})
    return HttpResponse(obj)


def index(request):
    """
    @summary: 处理index页面，返回指向待爬取网页的Request列表
    @param request:请求
    @return:页面的模板
    """
    # blog_list = BlogsPost.objects.all()
    # user = User.objects.create_superuser(username="admin1",email=None,password="admin")
    # user.save()
    response = render_to_response('apiIndex.html')
    response.set_cookie("username", 'test')
    return response


def apiList(request):
    """
    @summary: 处理apiList页面，返回指向待爬取网页的Request列表
    @param request:请求
    @return:页面的模板
    """
    # api_list = APIReference.objects.all()
    api_list = APIReference.objects.filter(enabled__exact=True)
    context = {
        'api_list' : api_list,
    }
    return render_to_response('apiList.html', context)


def apiCategory(request, param1):
    #print(param1)
    api_list = APIReference.objects.filter(APIService_category__exact=param1)
    context = {
        'api_list' : api_list,
    }
    return render_to_response('apiList.html', context)


def apiDetail(request, param1):
    #http://10.103.240.194:8080/accontroller/apiAccessControl?apiName=weather&userId=15
    api = APIReference.objects.get(name = param1)
    username = get_username(request)
    person = ConsumerReference.objects.get(username = username)
    status = 0
    if request.method == "POST":
        p = Userinfo.objects.get(username=username)
        payload = {'apiName': param1, 'userId': p.userid}
        try:
            req_content = get("http://10.103.240.194:8080/accontroller/apiAccessControl", params=payload, timeout=2)
            json_content = json.loads(req_content.content)
            if not(json_content['result']):
                return HttpResponse('3')
        except:
            return HttpResponse("2")
        try:
            new_buy = BuyReference(api=api,consumer=person)
            new_buy.save()
            Acl = AclReference(consumer=person, group=param1)
            Acl.save()
            #print(person.id)
            client = factory.get_kong_client()
            obj = ConsumerReference.objects.get(id=person.id)
            logic.synchronize_consumer(client, obj, toggle=False)
            client.close()
            return HttpResponse("1")
        except:
            return HttpResponse("2")
    api_key = person.keyauthreference_related.all()[:1]
    api_key = api_key[0]
    gateway_url = 'http://10.33.6.199:8000'
    url_Parameters = ParameterReference.objects.filter(api__name__exact = param1)
    Headers = HeaderReference.objects.filter(api__name__exact = param1)
    Errors  = ErrorReference.objects.filter(api__name__exact = param1)
    url_example = "?"
    for para in url_Parameters:
        url_example += para.name + '=' + para.defaultValue + '&'
    context = {
        'api' : api,
        'gateway_url' : gateway_url,
        'url_Parameters' : url_Parameters,
        'url_example' : url_example,
        'Headers' : Headers,
        'Errors' : Errors,
        'api_key': api_key,
        'status' : status,
    }
    return render_to_response('apiDetail.html', context)


def userCenter(request):
    # username = request.COOKIES.get('username', '')
    username = get_username(request)
    if not username:
        return HttpResponseRedirect('/api/')
    person = ConsumerReference.objects.get(username = username)
    p = Userinfo.objects.get(username=username)
    apis = person.infos.all()
    buy_apis = person.Buy_consumer.all()
    # for i in buy_apis:
    #     print(i.api)
    context = {
        'my_apis':apis,
        'buy_apis':buy_apis,
        'userID':p.userid,
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


def registerApi(request):
    if request.method == "POST":
        info = request.POST.copy()
        parameter = info['parameter']
        del info['parameter']
        form = APIForm(info, request.FILES)
        if form.is_valid():
            # username = request.COOKIES.get('username', '')
            username = get_username(request)
            API_new = form.save(commit=False)
            API_new.request_path = '/' + API_new.name
            API_new.strip_request_path = True
            API_new.owner = ConsumerReference.objects.get(username = username)
            API_new.save()
            ConfigPara(API_new, parameter)
            ConfigPlugin(API_new)
            message = u"API名:"+str(API_new.name)+'\n'
            message +=  u"API中文名"+API_new.APIChineseName+'\n'
            message += u"API信息:\n" + str(model_to_dict(API_new))
            send_mail(u'用户'+str(username)+u'发布了一个新的API', message, 'bupt2012211305@sina.com',
                      ['845842278@qq.com'], fail_silently=False)
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
        #print(dict['apiName'])
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
        json_dict['head'] = head_dict
        #print(json.dumps(json_dict))
        return HttpResponse(json.dumps(json_dict))



def modifyApi(request, param1):
    #print(param1)
    api = APIReference.objects.get(name=param1)
    if request.method == "POST":
        info = request.POST.copy()
        parameter = info['parameter']
        #print(parameter)
        del info['parameter']
        form = APIForm_modify(info, request.FILES, instance=api)
        if form.is_valid():
            username = get_username(request)
            # username = request.COOKIES.get('username', '')
            API_new = form.save(commit=False)
            API_new.save()
            ConfigPara(API_new, parameter)
            ConfigPlugin(API_new)
            message = u"API名:"+str(API_new.name)+'\n'
            message +=  u"API中文名"+API_new.APIChineseName+'\n'
            message += u"API信息:\n" + str(model_to_dict(API_new))
            send_mail(u'用户'+ str(username) + u'修改了一个API', message, 'bupt2012211305@sina.com',
                      ['845842278@qq.com'], fail_silently=False)
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
        #(dict['apiName'])
        api = APIReference.objects.get(name=dict['apiName'])
        #print(api)
        api.delete()
        return HttpResponseRedirect('/userCenter/')


def ConfigConsumer(username):
    consumer = ConsumerReference(username=username)
    consumer.save()
    KeyAuth = KeyAuthReference(consumer=consumer)
    KeyAuth.save()
    client = factory.get_kong_client()
    obj = ConsumerReference.objects.get(id=consumer.id)
    logic.synchronize_consumer(client, obj, toggle=False)
    client.close()

def registerConsumer(request):
    if request.method == "GET":
        #print(request.GET)
        name = request.GET.get('name')
        back = request.GET.get('callback')
        #print(name)
        d = {}
        d['message'] = '1'
        obj = json.dumps(d)
        if name:
            ConfigConsumer(name)
        else:
            send_mail(u"创建用户"+name+u"失败", message, 'bupt2012211305@sina.com',
                      ['845842278@qq.com'], fail_silently=False)
            return HttpResponse("field")
        return HttpResponse(str(back+'('+ obj+')'))

def apiHandler(request):
    pass

def apiFooter(request):
    return render_to_response('model/apiFooter.html')


def apiHeader(request):
    return render_to_response('model/apiHeader.html')