#ques 1 & ques 2
l1=[]
for x in range(0,5):
    st=str(input('Enter the element'))
    l1.append(st)
print(l1)
#ques 3
l2=[1,2,3,4,2,3,45,4]
print(l2.count(4))
#ques 4
l2.sort()
print(l2)
#ques 5
l3=[4,5,9,8,2,6,78,56,23,45]
l2.extend(l3)
l2.sort()
print(l2)
#ques 6 (stack)
stack=['Ram','Sham','Soumya']

c=1
while(c):
    print('Press 1 to append\nPress 2 to pop\nPress 3 to display\nPress 0 to end')
    c=int(input())
    if(c==1):
        s=input()
        stack.append(s)
    elif(c==2):
        stack.pop()
    elif(c==3):
        print(stack)
#ques 6 (queue)
a=0
c=1
queue=['Ram','Sham','Soumya']
while(c):
    print('Press 1 to append\nPress 2 to pop\nPress 3 to display\nPress 0 to end')
    c=int(input())
    if(c==1):
        s=input()
        queue.append(s)
    elif(c==2):
        queue.pop(a)

    elif(c==3):
        print(queue)


#ques 7
a=[10,42,65,23,78]
even=0
odd=0
for x in a:
    if(x%2==0):
        even+=1
    else:
        odd+=1
print('No. of even elements are %d\nNo. of odd elements are %d\n'%(even,odd))


##Tuples
##ques 1
t1=(4,5,6,8)
print(t1[::-1])
##ques 2
max=t1[0]
min=t1[0]
for x in t1:
    if(max<x):
        max=x
    if(min>x):
        min=x
print('Max=%d\n Min=%d'%(max,min))
##Strings
##ques 1
print('Enter a string\n')
a=input()
print(a.upper())
##ques 2
a=input()
print(a.isnumeric())
##ques 3
a='Hello World'
print(a.replace('World','Kausish'))



