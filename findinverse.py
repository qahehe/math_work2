#求a的逆元a' 
#其中a'a = b mod m 
#@author : 陈海龙

def egcd(a,b):  
    if b==0:  
        return 1,0  
    else:  
        x,y=egcd(b,a%b)  
        return y,x-a//b*y  
a=7
b=13
#例子 7x = 3 (mod 13)  得到7的乘法逆元为2 
ans1,ans2=egcd(a,b)
ans=(ans1*a+ans2*b)%b  #求最大公约数
if(ans==1):
    print(ans1," 是a的乘法逆元")
else:
    print("no answer,because no prime no inverse number")