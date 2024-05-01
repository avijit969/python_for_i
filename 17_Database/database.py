# name="isha"
# print(name)
import sqlite3
# import cx_Oralce

conn=sqlite3.connect("student.db")

cursor=conn.cursor()
q="""CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    age INTEGER,
    rollNo VARCHAR)"""
cursor.execute(q)

query= """INSERT INTO student (id,name,age,rollNo) VALUES (?,?,?,?)"""
data=[(2,"avi",19,969),
      (1,"isha",19,389),
      (3,"ram",1000,789)]

# cursor.execute(query,data) for single data insertion
# cursor.executemany(query,data)

# select data from table
query="SELECT * FROM student"

rows=cursor.execute(query)
print(list(rows))

for row in list(rows):
    print("student name is",row[1])
    print("student age is",row[2])
    print("student roll No is",row[3])

#delete data from table
query="DELETE FROM student WHERE id=?"
cursor.execute(query,(3,))

# update data from table
query="UPDATE student SET name=? WHERE id=?"
cursor.execute(query,("abhijit",2))

query="UPDATE student SET rollNo=? WHERE id=?"
cursor.execute(query,(898,2))

# select(searching) data with some condition 
query="SELECT * FROM student WHERE name=?"
# data=cursor.execute(query,("isha",))
# print(list(data))

conn.commit()
conn.close()
