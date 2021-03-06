/**
 * Created by lenovo on 2016/4/20.
 */
$(document).ready(function(){
    $("#header").load("/apiHeader");
    $(".nav-list").bind("click", function (event) {
        var node = event.target;
        if(node.tagName.toLowerCase() === "span"){
            node = node.parentNode;
        }
        $(node).addClass("active").siblings().removeClass("active");
        var $block = $(".block-cont");
        $block.each(function(){
            $(this).css("display", "none");
        });
        $block.eq($(node).index()).css("display","block");
    });

    $("#apiCategory").bind("change",function(){
        var value = Number($(this).val());
        if(value === 1){
            $("#fileDataName").show();
            $("#desWords").text("本平台数据提供型API，需要为API指定用于数据提供的数据文件名称，请填入数据名称输入栏中");
        }else if(value === 2){
            $("#fileDataName").hide();
            $("#desWords").text("本平台数据操作型API，所要操作的数据需要作为参数传入");
        }else if(value === 3){
            $("#fileDataName").hide();
            $("#desWords").text("平台纯功能型API，没有对平台数据文件的操作");
        }else if(value === 4){
            $("#fileDataName").hide();
            $("#desWords").text("外部注册型API，填写需要的参数和信息，本平台不会对其进行数据文件的日志记录");
        }
    });

    //对parameter的table添加事件  //删除按钮
    $("#apiParam").bind("click",function(event){
        var node = event.target;
        if(node.className.indexOf("btn-delete")!== -1){
            $(node).parent().parent().remove();
        }
        //说明最后一个也被删除
        var $tbodyTmp = $("#apiParam").find("tbody");
        if($tbodyTmp.find("tr").length === 0){
            var str = "<tr><td class='tc' colspan='6'>无请求参数</td></tr>";
            $tbodyTmp.append(str);
        }
    });
    $("#apiHeader").bind("click",function(event){
        var node = event.target;
        if(node.className.indexOf("btn-delete")!== -1){
            $(node).parent().parent().remove();
        }
        //说明最后一个也被删除
        var $tbodyTmp = $("#apiHeader").find("tbody");
        if($tbodyTmp.find("tr").length === 0){
            var str = "<tr><td class='tc' colspan='6'>无请求参数</td></tr>";
            $tbodyTmp.append(str);
        }
    });
    $("#apiErrorCode").bind("click",function(event){
        var node = event.target;
        if(node.className.indexOf("btn-delete")!== -1){
            $(node).parent().parent().remove();
        }
        //说明最后一个也被删除
        var $tbodyTmp = $("#apiErrorCode").find("tbody");
        if($tbodyTmp.find("tr").length === 0){
            var str = "<tr><td class='tc' colspan='4'>无错误码</td></tr>";
            $tbodyTmp.append(str);
        }
    });

    function addRowError(){
        var $tbodyTmp = $("#apiErrorCode").find("tbody");
        var length = $tbodyTmp.find("td").length;
        var str = '<tr><td> <input type="text" class="middle"> </td> ' +
            '<td><input type="text" class="middle"></td> ' +
            '<td><input type="text" class="middle"></td> ' +
            '<td><a class="btn-table btn-delete">删除</a></td></tr>';
        if(length === 1){
            $tbodyTmp.find("tr").remove();
        }
        $tbodyTmp.append(str);
    }
    function addRowParam(){
        var $tbodyTmp = $("#apiParam").find("tbody");
        var length = $tbodyTmp.find("td").length;
        var str = '<tr> <td> <input type="text" class="data-param-name" placeholder="英文"> </td> ' +
            '<td> <div class="select-fath data-param-type"> <select> <option value="string">string</option> <option value="number">number</option> <option value="boolean">boolean</option> </select> </div> ' +
            '</td> <td> <input type="text" class="data-param-desc" placeholder="填真实数据"> </td> ' +
            '<td> <input type="text" class="data-param-default" placeholder="填合法默认值"> </td> ' +
            '<td> <div class="select-path data-param-has-a"> <select> <option value="1">是</option> <option value="0">否</option> </select> </div> </td> ' +
            '<td> <a class="btn-table btn-delete">删除</a> </td> </tr>';
        if(length === 1){
            $tbodyTmp.find("tr").remove();
        }
        $tbodyTmp.append(str);
    }
    function addRowHeader(){
        var $tbodyTmp = $("#apiHeader").find("tbody");
        var length = $tbodyTmp.find("td").length;
        var str = '<tr> <td> <input type="text" class="data-param-name" placeholder="英文"> </td> ' +
            '<td> <div class="select-fath data-param-type"> <select> <option value="string">string</option> <option value="number">number</option> <option value="boolean">boolean</option> </select> </div> ' +
            '</td> <td> <input type="text" class="data-param-desc" placeholder="填真实数据"> </td> ' +
            '<td> <input type="text" class="data-param-default" placeholder="填合法默认值"> </td> ' +
            '<td> <div class="select-path data-param-has-a"> <select> <option value="1">是</option> <option value="0">否</option> </select> </div> </td> ' +
            '<td> <a class="btn-table btn-delete">删除</a> </td> </tr>';
        if(length === 1){
            $tbodyTmp.find("tr").remove();
        }
        $tbodyTmp.append(str);
    }

    //添加按钮
    $("#errorCode").bind("click",addRowError);
    $("#btnParameter").bind("click",addRowParam);
    $("#btnHeader").bind("click",addRowHeader);

    //下一步按钮
    $("#next").bind("click", function(){
        var $listTmp = $(".nav-list").find("li");
        $listTmp.eq(0).removeClass("active");
        $listTmp.eq(1).addClass("active");
        $(".block-cont").eq(0).css("display","none");
        $(".block-cont").eq(1).css("display","block");
    });
    $("#pre").bind("click", function(){
        var $listTmp = $(".nav-list").find("li");
        $listTmp.eq(1).removeClass("active");
        $listTmp.eq(0).addClass("active");
        $(".block-cont").eq(1).css("display","none");
        $(".block-cont").eq(0).css("display","block");
    });

    //=============================API列表的导航==========================//



    //=============================用户中心的操作=========================//

    //用户中心tab标签切换
    $(".aside-navi").bind("click",function(event){
        var node = event.target;
        if(node.tagName.toLocaleLowerCase() === 'a'){
            $(node).parent().siblings().find("a").each(function(){
                $(this).removeClass("active");
            });
            $(node).addClass("active");
            var num = $(node).parent().index();
            $(".usercenter-show").each(function () {
                $(this).css("display","none");
            });
            $(".usercenter-show").eq(num-1).css("display","block");
        }
    });

    //=============================API详情tab标签切换=======================//
    $(".tabs li").bind("click",function(){
        $(this).addClass("active").siblings().removeClass("active");
        var $frames = $(".frame");
        $frames.css("display","none");
        $frames.eq($(this).index()).css("display", "block");
    });

    $(".get-apikey").bind("click",function(){
        //使用ajax得到此用户的apikey
        //若此用户没有登录，则跳转到登录界面
        //$.ajax(function () {
        //
        //});
        $("#apikey").text("用户的apikey");

        $("#jquery-msg-overlay").show();
    });

    $("#overlayConfirm").bind("click",function(){
        $("#jquery-msg-overlay").hide();
    });
});