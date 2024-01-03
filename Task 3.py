import mysql.connector
conn=mysql.connector.connect(host='localhost',password='gagan123',user='root')
 
cursor = conn.cursor()
cursor.execute("""
    use studentdata
    
""")
 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
""")

# Insert a new student record
cursor.execute("""
    INSERT INTO students (first_name, last_name, age, grade)
    VALUES (%s, %s, %s, %s)
""", ("Alice", "Smith", 18, 95.5))

# Update the grade of the student with the first name "Alice"
cursor.execute("""
    UPDATE students
    SET grade = %s
    WHERE first_name = %s
""", (97.0, "Alice"))

# Delete the student with the last name "Smith"
cursor.execute("""
    DELETE FROM students
    WHERE last_name = %s
""", ("Smith",))

# Fetch and display all student records
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

for student in students:
    print(student)

# Commit and close the connection
conn.commit()
conn.close()
