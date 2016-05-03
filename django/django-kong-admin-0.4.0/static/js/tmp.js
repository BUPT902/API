/**
 * Created by lenovo on 2016/4/24.
 */
function QPL(arr){
    if(arr.length==1){//只有一个排序
        return arr;
    }else if(arr.length==2){//两个排序
        return [''+arr[0]+arr[1],''+arr[1]+arr[0]];
    }else{
        var tmp = [];
        for(var j=0;j< arr.length;j++){
            var pre = arr.splice(j,1);//取出arr[j]
            var m = QPL(arr);//递归排列arr[0],arr[1],...,arr[j-1],arr[j+1],...,arr[n]
            arr.splice(j,0,pre);//将arr[j]放入数组，保持原来的位置
            for(var i=0;i< m.length;i++){
                tmp.push(arr[j]+m[i]);//将arr[j]组合起来
            }
        }
        return tmp;
    }
}
//M590NS
Function.prototype.a = 1;
var a = new Function();
a.prototype.a = 2;
var c = new a();
console.log(a.a+","+ c.a);