#Assignments-SQL
#Answer-1
import sqlite3
'''
try:
    con=sqlite3.connect('rajan.db')#connecting with database
    cursor=con.cursor()#creating an object
    query='create table Student(id int(5) primary key,name varchar(10),marks int(10))'#Query
    cursor.execute(query)
    print('Students table is created')
    con.commit()
except sqlite3.DatabaseError as er:
    if con:
        con.rollback()
        print('Problem occured: ', er)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        '''
#Answer-2,#Answer3
try:
    con=sqlite3.connect('rajan.db')
    cursor=con.cursor()
    for i in range(1,11):
        a=int(input('enter id'))
        b=input('enter name')
        c=int(input('enter subject marks'))
        if c<=100:
            queries="insert into Student(id,name,marks) values(?,?,?)"#entering marks and names to columns created already
            val=(a,b,c)
            cursor.execute(queries,val)
        else:
            print('enter valid marks')
    con.commit()
    print('values entered successfuly')
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e) 
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()       
    print('enterd')
#Answer-4 print students with marks>=60
try:
    con = sqlite3.connect('rajan.db')
    
    cursor = con.cursor()
    
    query = 'select * from Student'
    
    cursor.execute(query)
    
    data = cursor.fetchall()
    
    for row in data:
        if row[2]>=60:
            print('id: {},name: {}, marks: {}'\
             .format(row[0], row[1], row[2]))
    
except sqlite3.DatabaseError as e:
       if con:
          con.rollback()
          print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')    
