import pandas as pd

students = {
 "name": ["Ravi", "Sita", "Kiran"],
 "course": ["Python", "Java", "DevOps"],
 "marks": [80, 90, 75]
}

df=pd.DataFrame(students)
print(df)
print(df.ndim)
print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())


df.to_excel("students.xlsx", index=False)

print("excel file created successfully")

print("============  start reading excel data ============")
newDf=pd.read_excel("students.xlsx")
print(newDf)