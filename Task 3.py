#task 3:MYSQL Database operations with Python
#creating a database

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prateek@8979",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

#creating a table
mycursor.execute("CREATE TABLE Students ( Student_id int PRIMARY KEY, First_name VARCHAR(30), Last_name VARCHAR(30), Age INT,Grade INT)")

#inserting the data into table

data = "INSERT INTO Students (Student_id, First_name, Last_name, Age, Grade) VALUES (%s, %s, %s, %s, %s)"
val = ("1", "Alice","Smith","18","95.5")
mycursor.execute(data, val)
mydb.commit()

#updating the grade of the student with  first name alice

data = "UPDATE Students SET Grade = '97' WHERE First_name = 'Alice'"
mycursor.execute(data)
mydb.commit()

#deleting the student with last name smith

data = "DELETE FROM Students WHERE Last_name = 'Smith'"
mycursor.execute(data)
mydb.commit()

#fetch and display all student records

mycursor.execute("SELECT * FROM Students")
final = mycursor.fetchall()
for x in final:
    print(x)
