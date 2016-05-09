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


# class ParamForm(forms.ModelForm):
#
#     class Meta:
#         exclude = ['api']
#         model = ParameterReference
#         widgets = {
#             'name' : forms.TextInput(attrs={'class': 'data-param-name',
#                                             'placeholder' : u'英文',
#                                             }),
#             'type': forms.TextInput(attrs={'class':"select-fath data-param-type",
#                                         }),
#             'description' : forms.TextInput(attrs={'class' : "data-param-desc",
#             }),
#             'defaultValue' : forms.TextInput(attrs={'class':'data-param-default'}),
#             'id' :  forms.TextInput(attrs={'type':'hidden',},)
#         }


class APIForm(forms.ModelForm):

    class Meta:
        model = APIReference
        exclude = ['owner', 'request_path', 'request_host', 'preserve_host', 'strip_request_path']
        widgets ={
            'APIChineseName' : forms.TextInput(attrs={'placeholder': u'请输入API中文名称'}),
            'API_description' : forms.Textarea(attrs={'class':'api-long apiSimpleIntro',
                                                      'placeholder':u"""详细描述下吧，API的功能等信息\n\n示例：快递查询API，覆盖国内外100余家快递公司业务中的公司名称、快递电话、快递进度等信息。\n包含数据项为：缓存时间（当前时间与 update 之间的差值）、快递进度、快递公司英文代码、快递公司中文名、快递单号、快递电话、最后更新时间等数据项。\n可用于快递信息查询、快递派送路线分析及优化、快递公司效率对比与选择、快递公司经营分析与优化、快递大户搜索统计，快递物品分析及营销投放、快递效率优化、快递公司快递员KPI、快递公司电话查询、经济景气指数建立与预测等。"""
                                                      }),
            'APIShort_description' : forms.Textarea(attrs={'class':'mt15 api-long apiSimpleIntro',
                                                           'style':'height: 60px',
                                                           'placeholder':u"""简要描述下你的API吧，便于更快的检索\n\n示例：快递查询API，覆盖国内外100余家快递公司业务中的公司名称、快递电话、快递进度等信息。"""
                                                           }),
            'name' : forms.TextInput(attrs={'placeholder':u'请输入API英文名称'}),
            'upstream_url':forms.URLInput(attrs={'placeholder':'请写不含参数的url'}),
            'requestType' : forms.RadioSelect(attrs={'class':'mt15'}),
            'returnSample' : forms.Textarea(attrs={'class':'api-long',
                                                   'placeholder':
                                                                """JSON响应示例：
                                                            {
                                                            "errNum": 0,//错误码
                                                                "errMsg": "success", //返回结果提示信息
                                                                "retData": {
                                                                    "phonenum": "15210011578",//手机号
                                                                    "province": "北京",  //所属省份
                                                                    "carrier": "北京移动" //运营商
                                                                }
                                                            }"""
                                                   }),
            'remake' : forms.Textarea(attrs={'class':'api-long'})

        }


def ConfigPlugin(API):
    obj = json.dumps({'time': '1'})
    plugin = PluginConfigurationReference(api=API, plugin=2, config=obj)
    plugin.save()


def ConfigPara(API, parameter):
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