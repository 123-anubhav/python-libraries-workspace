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
print(df.describe())
print(df.tail())

info=df.info()
print("Df info ::->",info)

df.to_csv("students.csv", index=False)

print("CSV file created successfully")

print("============  start reading csv data ============")
df=pd.read_csv("students.csv")

print(df)