import sqlite3

sqliteConnection = sqlite3.connect('test.db')

cursor = sqliteConnection.cursor()

print("Connected to the database")

# sql_command = """CREATE TABLE emp ( 
# staff_number INTEGER PRIMARY KEY, 
# fname VARCHAR(20), 
# lname VARCHAR(30), 
# gender CHAR(1), 
# joining DATE);"""
# cursor.execute(sql_command)

# primary key
pk = [2, 3, 4, 5, 6]
 
# Enter 5 students first names
f_name = ['Nikhil', 'Nisha', 'Abhinav', 'Raju', 'Anshul']
 
# Enter 5 students last names
l_name = ['Aggarwal', 'Rawat', 'Tomar', 'Kumar', 'Aggarwal']
 
# Enter their gender respectively
gender = ['M', 'F', 'M', 'M', 'F']
 
# Enter their joining data respectively
date = ['2019-08-24', '2020-01-01', '2018-05-14', '2015-02-02', '2018-05-14']
 
for i in range(5):
 
    # This is the q-mark style:
    cursor.execute('INSERT INTO emp VALUES (?, ?, ?, ?, ?)', (pk[i], f_name[i], l_name[i], gender[i], date[i]))


sqliteConnection.commit()
# close the connection
sqliteConnection.close()