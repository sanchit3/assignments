#Assignment
#Answer-1
import pymongo
client = pymongo.MongoClient()
database = client['rajan']
collection = database['Students']
#Answer-2,Answer-3
for i in range(1,11):
    a=input('enter name')
    b=int(input('enter marks'))
    collection.insert_one({"Names":a,"Marks":b})#inserting values
#Answer-4
data = collection.find()#FETCH ALL DATA
for ds in data:
    if ds[1]>60:#compare marks
        print(ds[0])#print name
    
