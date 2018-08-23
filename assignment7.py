##Ques 1
dict={'apple':5,'orange':10,'lemon':15,'kiwi':20}
for a,b in dict.items():
    print(a)

##Ques 2
student={'Rishabh':{'eng':100,'hindi':100,'Punjabi':99},'Naina':{'eng':93,'hindi':95,'Punjabi':97}\
    ,'Arushka':{'eng':98,'hindi':81,'Punjabi':73}}
st=input("Enter the name whose marks u wanna fetch")

if(student[st]):
    for a,b in student[st].items():
        print('Marks in {} is {}'.format(a,b))
else:
    print('Sorry the student with this name is not present in the class')