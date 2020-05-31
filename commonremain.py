def egcd(a,b):  
    if b==0:  
        return 1,0  
    else:  
        x,y=egcd(b,a%b)  
        return y,x-a//b*y  
a=133
b=210
m=280
ans1,ans2=egcd(a,m)
ans=(ans1*a +m*ans2)%m #ans=d
ans3,ans4=egcd(a,b)
res=(ans3*a +b*ans4)%b
L=[]
if(ans==1):  #当gcd(a,m)=1时，m>0，同余方程恰有一个解
    print(ans1, " 是a的乘法逆元")
    b= (b*ans1)%m
    print("同余方程为：x = ",b," mod ",m," ")
else:
    if(res==ans):
        if(ans%b):#当gcd(a,m)！=1时，m>0，同余方程恰有d个解
            i=1
            x0= ans1*(b//ans)%m
            while(i<=res):
                L.append((x0+(i-1)*m//res)%m)
                i=i+1
            i=1
            while(i<=res):
                print("同余方程解为x = ",x0," + (",i-1,")*",m//res)
                i=i+1
        else:
            print("no answer,because no prime no inverse number")
    else:
        print("no answer,because no prime no inverse number")

