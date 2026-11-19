import sqlite3

conn = sqlite3.connect("studentA.db")
cursor = conn.cursor()

print("===STUDENT RESULT MANAGEMENT===")

print('1.Add student')
print('2.View students')
print('3.Add subject')
print('4. Add marks')
print('5.Update marks')
print('6.Delete students')
print('7.Show student result')
print('8.Class topper')
print('9.Average marks')
print('10.Search student')
print('11.Exit')

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    student_id INT PRIMARY KEY ,
    name VARCHAR (50),
    age INT,
    student_class VARCHAR (20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS subject (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS marks (
    student_id INT,
    subject_id INT,
    marks INT,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id)
)
""")

def add_student():
    student_id = int(input("Enter ID: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    student_class = (input("Enter class: "))

    cursor.execute("""                   
    INSERT INTO student (student_id,name,age,    student_class)   
    VALUES(?,?,?,?)  
    """, (student_id,name,age,student_class))  
  
    conn.commit()     
    print("Student added successfully!")

#××××××

def add_subject():
    subject_id = int(input("Enter Subject_id: "))
    subject_name = input("Enter subject: ")

    cursor.execute("""                                                     INSERT INTO subject (subject_id,subject_name)  
    VALUES(?,?)  
    """,(subject_id,subject_name))  
  
    conn.commit()  
    print("Subject added successfully!")

#××××××

def add_marks():
    student_id = int(input("Enter student_id: "))
    subject_id = int(input("Enter subject_id: "))
    marks = int(input("What are your marks: "))

    cursor.execute("""  
    INSERT INTO marks (student_id,subject_id, marks)  
    VALUES(?,?,?)  
    """,(student_id,subject_id,marks))  
  
    conn.commit()  
    print("Marks added successfully!")

#×××××

def view_student():
    cursor.execute(
    "SELECT * FROM student;"
    )
    students = cursor.fetchall()

    for student in students:  
        print(student)  
      
    if not students:  
        print("No students found.")

#×××××××

def view_subject():
    cursor.execute(
    "SELECT * FROM subject;"
    )
    subjects = cursor.fetchall()

    for subject in subjects:  
        print(subject)  
  
    if not subjects:  
        print("No subjects found.")

#×××××

def view_marks():
    cursor.execute(
    "SELECT * FROM marks;"
    )
    marks = cursor.fetchall()

    for mark in marks:  
        print(mark)    
      
    if not marks:  
        print("No marks.")

#×××××××

def update_marks():
    student_id = int(input("Enter your student_id: "))
    subject_id = (input("which subject: "))
    new_marks = int(input("What are your updated marks: "))

    cursor.execute("""          
    UPDATE marks SET marks = ? 
    WHERE  subject_id = ? AND student_id = ?  
    """,(new_marks,subject_id,student_id))  
  
    conn.commit()     
    print("Marks Updated.")

#××××××

def delete_student():
    student_id = int(input("Enter student_id: "))

    cursor.execute(  
    "DELETE FROM student WHERE student_id = ?",  
    (student_id,)  
    )  
  
    conn.commit()  
    print("Student deleted.")

#××××××

def show_student_result():
    student_id = int(input("Enter Student ID: "))

    cursor.execute("""
    SELECT s.student_id , s.name , sub.subject_name , m.marks
    FROM student as s
    JOIN marks as m ON s.student_id = m.student_id
    JOIN subject as sub ON sub.subject_id = m.subject_id
    WHERE s.id = ? ;
    """,(student_id,))

    result = cursor.fetchall()

    if result:
        print("== Student Result ==")

    for row in result:  
        print(row)

    else:
        print("Student result not found.")

#×××××

def class_topper():
    cursor.execute("""
    SELECT s.student_id , s.name , m.marks 
    FROM student AS s 
    JOIN  marks AS m 
    ON s.student_id = m.student_id 
    ORDER BY m.marks DESC 
    LIMIT 1
     """)
    topper = cursor.fetchone()

    if topper:  
        print("class topper: ")  
        print(topper)                            
    else:  
        print("no topper found.")

#×××××

def average_marks():
    cursor.execute("""
    SELECT avg(marks) FROM marks
    """)
    
    average = cursor.fetchone()
    if average[0] is not None:
        print("Average Marks:", round(average[0], 2))
    else:
        print("No marks found.")
#××××

def search_student():
    student_id = int(input("Enter your student_id: "))

    cursor.execute("""                          
    SELECT * FROM student WHERE  student_id = ?  
    """,(student_id,))     

    student = cursor.fetchone()  
  
    if student:  
        print(student)  
    else:  
        print("Student not found.")

#××××
def student_result_display():
    student_id = int(input("Enter student_id: "))
    
    cusor.execute("""    
    SELECT sub.subject_name,m.marks 
    FROM subject AS sub
    JOIN marks AS m ON sub.student_id = m.student_id
    WHERE m.student_id = ? 
    """,(student_id,))
    
    result = cursor.fetchall()
    
    cursor.execute("""
    SELECT SUM(marks) 
    FROM marks
    WHERE student_id = ?
    """,(student_id,))
    
    total = cursor.fetchone()
    
    cursor.execute("""
    SELECT AVG(marks) 
    FROM marks
    WHERE student_id= ? 
    """,(student_id,))
    
    avg = cursor.fetchone()
    print("\n--- Report Card ---")
    
    for subject_name,marks in result:
        print(subject_name,marks)  
        
    print("Total:", total[0])
    print("Average:", avg[0])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                           
while True:
    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        add_subject()
    elif choice == 4:
        add_marks()
    elif choice == 5:
        view_subject()
    elif choice == 6:
        view_marks()
    elif choice == 7:
        update_marks()
    elif choice == 8:
        delete_student()
    elif choice == 9:
        show_student_result()
    elif choice == 10:
        class_topper()
    elif choice == 11:
        average_marks()
    elif choice == 12:
        search_student()
    elif choice == 13:
        exit()
    else:
        print("INVALID CHOICE!")

#start again after learning oops.