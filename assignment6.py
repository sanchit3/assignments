##Ques 1
pi=3.14
def area(r):
    return (4*3.14*r**2)
radius=int(input('Enter the radius:'))
ans=area(radius)
print(ans)

##ques 2

def perfect():
    for x in range(1,1001):
        a=1
        check=0
        while a<=int(x/2):
            if(x%a==0):
                check+=a
            a+=1
        if(check==x):
            print(x)
perfect()

## Ques 3
def table(n):
    for x in range(1,11):
        print(n*x)
num=int(input('Enter the no.:'))
table(num)
##Ques 4

num=int(input())
mul=int(input())
def mu(num,mul):
    while(mul!=0):
        if mul==1:
            return num
        else:
            return num*mu(num,mul-1)
a=mu(num,mul)
print(a)


