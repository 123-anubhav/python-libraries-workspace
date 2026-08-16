import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

sql="""   
    create table if not exists students(
 student_id integer primary key autoincrement,
 student_name text,
 student_email text unique,
 student_course text,
 student_fee real
 )
"""

data = cursor.execute(sql)
print("Student Table Created Successfully....")
connection.commit()
connection.close()
