import sqlite3 as sql

conn = sql.connect('User.db')
cursor = conn.cursor()

statement = '''SELECT * FROM user'''
  
cursor.execute(statement) 

values = cursor.fetchall()

s = input('Enter the username:')
p = input('Enter the password:')

check = 1
for i in values:
    if s == i[1]:
        if p == i[2]:
            print('Login Successful')
        else:
            print('Wrong password')
        
        

conn.commit()
conn.close()