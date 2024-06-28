import sqlite3 as sql

def studentData():
    conn = sql.connect("Student.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, f_name text, l_name text, Age text)")
    conn.commit()
    conn.close()

def addrecord(StdID, f_name, l_name, Age):
    conn = sql.connect("Student.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?)",StdID, f_name, l_name, Age)
    conn.commit()
    conn.close()

def viewdata():
    conn = sql.connect("Student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    row = cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn = sql.connect("Student.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    conn.commit()
    conn.close()

def search(StdID="",f_name="",l_name="",Age=""):
    conn = sql.connect("Student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR f_name=? OR l_name=? OR Age=?",(StdID,f_name,l_name,Age))
    row = cur.fetchall()
    conn.close()
    return row

def Update(id, StdID="",f_name="",l_name="",Age=""):
    conn = sql.connect("Student.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET StdId=?, f_name=?, l_name=?, Age=?, id=?",(StdID,f_name,l_name,Age,id))
    conn.commit()
    conn.close()

studentData()