#求x的同余方程
# ax = b mod m
# @author :陈海龙
def egcd(a,b):  
    if b==0:  
        return 1,0  
    else:  
        x,y=egcd(b,a%b)  
        return y,x-a//b*y  
a=7
b=3
m=13
ans1,ans2=egcd(a,m)
ans=(ans1*a +m*ans2)%m
if(ans==1):  #a,m互素才有逆元
    print(ans1, " 是a的乘法逆元")
else:
    print("no answer,because no prime no inverse number")
b= (b*ans1)%m
print("同余方程为：x = ",b," mod ",m," ")
