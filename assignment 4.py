##Ques 1
st=[1,2,3,4,5]
st.reverse()
print("The reversed list is " ,st)

##ques 2
st=input("Enter the string from which u want to take out upper characters\n")
for x in st:
    if x.isupper():
        print(x,end=" ")

##ques 3

l=input()##input should be no.s separted by commas like 45,56,89,56
a=l.split(',')
l2=[]
for x in a:
    b=int(x)
    l2.append(b)
print(l2)



##ques 4
l=input()
l2=l[::-1]
if l==l2:
    print ('palindrome')
else:
    print('Not palindrome')

##ques 5
l1= [1, 2, [3,5], 4]
l2= copy.deepcopy(l1)
print(l1)
l2[2][0] = 7
print(l2)
# Change is NOT reflected in original list l1
# as it is a deep copy
print(l1)

#diff between deep and shallow copy:
#1. In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
#  In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.
#2.In python, this is implemented using “deepcopy()” function.
#   In python, this is implemented using “copy()” function.
#3.*******************************************************
#l1= [1, 2, [3,5], 4]
#l2= copy.deepcopy(l1)
#print(l1)
#l2[2][0] = 7
#print(l2)
# Change is NOT reflected in original list l1 # as it is a deep copy
#print(l1)
#output:
#1 2 [3, 5] 4
#1 2 [7, 5] 4
#1 2 [3, 5] 4
#**********************************
#li1 = [1, 2, [3,5], 4]/////eg of shallow cpy
#li2 = copy.copy(li1)
#print(li1)
#li2[2][0] = 7
#print(li1)
#output
#1 2 [3, 5] 4
#1 2 [7, 5] 4