/**
 * Created by lenovo on 2016/4/24.
 */
function QPL(arr){
    if(arr.length==1){//ֻ��һ������
        return arr;
    }else if(arr.length==2){//��������
        return [''+arr[0]+arr[1],''+arr[1]+arr[0]];
    }else{
        var tmp = [];
        for(var j=0;j< arr.length;j++){
            var pre = arr.splice(j,1);//ȡ��arr[j]
            var m = QPL(arr);//�ݹ�����arr[0],arr[1],...,arr[j-1],arr[j+1],...,arr[n]
            arr.splice(j,0,pre);//��arr[j]�������飬����ԭ����λ��
            for(var i=0;i< m.length;i++){
                tmp.push(arr[j]+m[i]);//��arr[j]�������
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