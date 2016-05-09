/**
 * Created by lenovo on 2016/5/9.
 */
//此脚本加载时，得到要修改的API的名称，具体发送不发送。看得到的val是不是null;
$(document).ready(function(){
    var editApiName = $("#id_name").val();
    //说明是发布API，不需要发送请求
    if(editApiName !== ""){
        $.ajax({
            type: "GET",
            url: "/edit-api/",
            data: {
                apiName: editApiName
            },
            success: function(response){
                //var response = '{"head": {"param1": {"nessesary": false, "description": "API-key", "defaultValue": "\u65e0", "api_id": 4, "type": "number", "id": 3, "name": "key"}, "param0": {"nessesary": true, "description": "\u57ce\u5e02\u540d\u79f0\uff0c\u56fd\u5185\u57ce\u5e02\u652f\u6301\u4e2d\u82f1\u6587\uff0c\u56fd\u9645\u57ce\u5e02\u652f\u6301\u82f1\u6587", "defaultValue": "beijing", "api_id": 4, "type": "string", "id": 2, "name": "city"}}, "param": {"param1": {"nessesary": true, "description": "API-key", "defaultValue": "\u65e0", "api_id": 4, "type": "string", "id": 3, "name": "key"}, "param0": {"nessesary": true, "description": "\u57ce\u5e02\u540d\u79f0\uff0c\u56fd\u5185\u57ce\u5e02\u652f\u6301\u4e2d\u82f1\u6587\uff0c\u56fd\u9645\u57ce\u5e02\u652f\u6301\u82f1\u6587", "defaultValue": "beijing", "api_id": 4, "type": "string", "id": 2, "name": "city"}}, "error": {"err1": {"message": "err2", "code": 2, "id": 2, "api_id": 4, "description": "\u9519\u8bef2"}, "err0": {"message": "err1", "code": 1, "id": 1, "api_id": 4, "description": "\u9519\u8bef1"}}}';
                console.log(response);
                var obj = JSON.parse(response);
                $.each(obj, function(name,value){
                    if(name === "head"){
                        $.each(value, function(name,value){
                            editRowHeader(value.name, value.type, value.description, value.defaultValue, value.nessesary);
                        });
                    }else if(name === "param"){
                        $.each(value, function(name,value){
                            editRowParam(value.name, value.type, value.description, value.defaultValue, value.nessesary);
                        });
                    }else{
                        $.each(value, function(name,value){
                            editRowError(value.code, value.message, value.description);
                        });
                    }
                });
            }
        });
    }

    function editRowHeader(name, type, description, defaultValue, nessesary){
        var $tbodyTmp = $("#apiHeader").find("tbody");
        var tmp = nessesary? 1 : 0;
        var length = $tbodyTmp.find("td").length;
        var str = '<tr> <td> <input type="text" class="data-param-name" value='+name+'> </td> ' +
            '<td> <div class="select-fath data-param-type"> <select> <option value="string">string</option> <option value="number">number</option> <option value="boolean">boolean</option> </select> </div> ' +
            '</td> <td> <input type="text" class="data-param-desc" value='+description+'> </td> ' +
            '<td> <input type="text" class="data-param-default" value='+defaultValue+'> </td> ' +
            '<td> <div class="select-path data-param-has-a"> <select> <option value="1">是</option> <option value="0">否</option> </select> </div> </td> ' +
            '<td> <a class="btn-table btn-delete">删除</a> </td> </tr>';
        if(length === 1){
            $tbodyTmp.find("tr").remove();
        }
        $tbodyTmp.append(str);
        $tbodyTmp.find("tr:last").find("td").eq(1).find('option[value='+type+']').attr("selected",true);
        $tbodyTmp.find("tr:last").find("td").eq(4).find('option[value='+tmp+']').attr("selected",true);
    }
    function editRowParam(name, type, description, defaultValue, nessesary){
        var $tbodyTmp = $("#apiParam").find("tbody");
        var tmp = nessesary? 1 : 0;
        var length = $tbodyTmp.find("td").length;
        var str = '<tr> <td> <input type="text" class="data-param-name" value='+name+'> </td> ' +
            '<td> <div class="select-fath data-param-type"> <select> <option value="string">string</option> <option value="number">number</option> <option value="boolean">boolean</option> </select> </div> ' +
            '</td> <td> <input type="text" class="data-param-desc" value='+description+'> </td> ' +
            '<td> <input type="text" class="data-param-default" value='+defaultValue+'> </td> ' +
            '<td> <div class="select-path data-param-has-a"> <select> <option value="1">是</option> <option value="0">否</option> </select> </div> </td> ' +
            '<td> <a class="btn-table btn-delete">删除</a> </td> </tr>';
        if(length === 1){
            $tbodyTmp.find("tr").remove();
        }
        $tbodyTmp.append(str);
        $tbodyTmp.find("tr:last").find("td").eq(1).find('option[value='+type+']').attr("selected",true);
        $tbodyTmp.find("tr:last").find("td").eq(4).find('option[value='+tmp+']').attr("selected",true);
    }
    function editRowError(code, message, description){
        var $tbodyTmp = $("#apiErrorCode").find("tbody");
        var length = $tbodyTmp.find("td").length;
        var str = '<tr><td> <input type="text" class="middle" value='+code+'> </td> ' +
            '<td><input type="text" class="middle" value='+message+'></td> ' +
            '<td><input type="text" class="middle" value='+description+'></td> ' +
            '<td><a class="btn-table btn-delete">删除</a></td></tr>';
        if(length === 1){
            $tbodyTmp.find("tr").remove();
        }
        $tbodyTmp.append(str);
    }
});