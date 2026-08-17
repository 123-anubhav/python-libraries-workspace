import pandas as pd

marks = pd.Series([10, 20, 15, 28, 45, 60])
print(marks)  # series is 1-D Column

print(marks.ndim)
print(marks.shape)
print(marks.dtypes)
print("default indexing :: => ",marks[0],marks[1],marks[2])

print("custom indexing example")

marks = pd.Series([10, 20, 15, 28, 45, 60], index=['a', 'b', 'c', 'd', 'e', 'f'])
print("custom indexing ::",marks['a'])
print("custom indexing ::",marks['f'])

marks = pd.Series([10, 20, 15, 28, 45, 60], index=[10, 20, 25, 15, 30, 12])
print("custom indexing with value ::",marks[15])
print("custom indexing  with value ::",marks[12])
# =============================================

students = {
 "name": ["Ravi", "Sita", "Kiran"],
 "course": ["Python", "Java", "DevOps"],
 "marks": [80, 90, 75]
}

print(students)
print(students["name"])


print("=============================================")

