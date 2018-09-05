##Ques 1
import re
h=input('Type your text:')
count=0
matcher=re.finditer('[a-zA-z][a-zA-Z0-9_.]*[@](gmail.com|yahoo.com|hotmail.com|outlook.com)',h)
for i in matcher:
    count+=1
    print('{} is a valid id'.format(i.group()))
if(count==0):
    print('Not valid')

##Ques 2

h=(input('Enter the no.:'))
count=0
matcher=re.finditer('[6-9][0-9]{9}',h)
for i in matcher:
    count+=1
    print('{} is a valid no.'.format(i.group()))
if(count==0):
    print('Not valid')