/**
 * Created by lenovo on 2016/5/9.
 */
//此脚本加载时，得到要修改的API的名称，具体发送不发送。看得到的val是不是null;
$(document).ready(function(){
    var editApiName = $("id_name").val();
    //$.ajax({
    //    type: "GET",
    //    url: "/edit-api/",
    //    data: {
    //        apiName: name
    //    },
    //    success: function(response){
    //
    //    }
    //});
    var response = '{"head": {"param1": {"nessesary": true, "description": "API-key", "defaultValue": "\u65e0", "api_id": 4, "type": "string", "id": 3, "name": "key"}, "param0": {"nessesary": true, "description": "\u57ce\u5e02\u540d\u79f0\uff0c\u56fd\u5185\u57ce\u5e02\u652f\u6301\u4e2d\u82f1\u6587\uff0c\u56fd\u9645\u57ce\u5e02\u652f\u6301\u82f1\u6587", "defaultValue": "beijing", "api_id": 4, "type": "string", "id": 2, "name": "city"}}, "param": {"param1": {"nessesary": true, "description": "API-key", "defaultValue": "\u65e0", "api_id": 4, "type": "string", "id": 3, "name": "key"}, "param0": {"nessesary": true, "description": "\u57ce\u5e02\u540d\u79f0\uff0c\u56fd\u5185\u57ce\u5e02\u652f\u6301\u4e2d\u82f1\u6587\uff0c\u56fd\u9645\u57ce\u5e02\u652f\u6301\u82f1\u6587", "defaultValue": "beijing", "api_id": 4, "type": "string", "id": 2, "name": "city"}}, "error": {"err1": {"message": "err2", "code": 2, "id": 2, "api_id": 4, "description": "\u9519\u8bef2"}, "err0": {"message": "err1", "code": 1, "id": 1, "api_id": 4, "description": "\u9519\u8bef1"}}}';
    var obj = JSON.parse(response);
    $.each(obj, function(name,value){
        if(name === "head"){
            $.each(value, function(name,value){
                //editRowHeader(value.name, value.type, value.description, value.defaultValue, value.nessesary);
                //(value.name);
            });
        }else if(name === "param"){

        }else{

        }
    });
    alert("apiName"+editApiName);
});