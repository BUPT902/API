#coding=utf-8
from django.shortcuts import render
from kong_admin.models import APIReference, ParameterReference, HeaderReference, ErrorReference, ConsumerReference, KeyAuthReference
from django.shortcuts import render_to_response,  HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from kong_admin.views import synchronize_api_reference, synchronize_api_references, synchronize_consumer_reference, \
    synchronize_consumer_references
import json


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
    gateway_url = 'http://localhost:8000'
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
    for i in buy_apis:
        print(i.api)
    context = {
        'my_apis':apis,
        'buy_apis':buy_apis,
    }
    return render_to_response('userCenter.html', context)


def delete_api(request):
    if request.method == "POST":
        dict = request.POST.dict()
        print(dict['apiName'])
        api = APIReference.objects.get(name=dict['apiName'])
        print(api)
        api.delete()
        HttpResponseRedirect('/userCenter/')
        # return HttpResponse('11232')


def registerApi(request):
    return render_to_response('registerApi.html')


def apiFooter(request):
    return render_to_response('model/apiFooter.html')


def apiHeader(request):
    return render_to_response('model/apiHeader.html')