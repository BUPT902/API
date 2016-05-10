#coding=utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from kong_admin.models import APIReference, ParameterReference, HeaderReference, ErrorReference, ConsumerReference, KeyAuthReference,\
    PluginConfigurationReference


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
            'remake' : forms.Textarea(attrs={'class':'api-long'}),
            'logo' : forms.FileInput(attrs={'id':'uploadBtn', 'type':'file', 'class':'upload'})

        }

class APIForm_modify(forms.ModelForm):

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
            'name' : forms.TextInput(attrs={'placeholder':u'请输入API英文名称', 'readonly':True, 'style':"background-color:#EBEBE4"},),
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
            'remake' : forms.Textarea(attrs={'class':'api-long'}),
            'logo' : forms.FileInput(attrs={'id':'uploadBtn', 'type':'file', 'class':'upload'})

        }
