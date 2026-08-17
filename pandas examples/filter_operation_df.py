import pandas as pd

employees = {
 "EmpId": [101, 102, 103, 104, 105, 106],
 "Name": ["Ravi", "Sita", "Kiran", "Rahul", "Priya", "Anil"],
 "Department": ["IT", "HR", "IT", "Sales", "HR", "IT"],
 "Salary": [50000, 45000, 70000, 40000, 48000, 65000],
 "Experience": [2, 5, 8, 1, 4, 7]
}

df = pd.DataFrame(employees)

print(df["EmpId"])
print(df["Name"])
print(df["Department"])
print(df["Salary"])

print("===============     SORTING FIELD `NAME`   ==========================")
sorted_data=df["Name"].sort_values(ascending=False)
print("desc sort by name field data",sorted_data)

sorted_data=df["Name"].sort_values(ascending=True)
print("Asc sort by name field data",sorted_data)

print("===============     SORTING Using 2 FIELD `Department` and  `Salary`  DESc: Salary and Asc: Department  ==========================")
df=df.sort_values(["Department","Salary"],ascending=[True,False])
print(df)


print("===============     SORTING Using 2 FIELD `Department` and  `Salary`  Asc: Salary and Asc: Department  ==========================")
df=df.sort_values(["Department","Salary"],ascending=[True,True])
print(df)

newDf=df[df["Salary"] >60000]
print(newDf)
print(newDf["EmpId"])
print(newDf["Name"])
print(newDf["Department"])

print("================  original df is ===========")
print(df)
print("=================== Salary and departemnt wise filter data using dataframe ===============\n")
newDf=df[(df["Salary"] >30000) & (df["Department"]=="IT")]
print(newDf)

print(" ======   Added One field `BONUS`  ==============  \n")
df["Bonus"]=df["Salary"]* 0.15

print(df)

print(" ======   Added One MoRe field `Total_Salary`  ==============  \n")
df["Total_Salary"]=df["Salary"]+df["Bonus"]
print(df)

print("===========  after perform updates on bonus in salary drop column ===========\n")
df.drop(columns=["Bonus"], inplace=True)
print(df)

print(df.nunique()) # give total unique data in df

print(" =================  Grouping In DataFrame  =======================")
print(df.groupby("Department")["Salary"].max())
print("----------------------------------------------------")
print(df.groupby("Department")["Salary"].min())

print("----------------------------------------------------")
print(df.groupby("Department")["Salary"].mean())

print("----------------------------------------------------")
print(df.groupby("Department")["Salary"].std())

print("----------------------------------------------------")
print(df["Department"].unique())

print("----------------------------------------------------")
print(df.groupby("Department")["Salary"].describe())


emps = {
 "Name":["Ravi","Sita","Kiran","Rahul"],
 "Salary":[50000,None,65000,None]
}

print("-------------------isnull and isnull().sum()----------------------------")
ndf = pd.DataFrame(emps)
print(ndf.isnull())
print("-------------------isnull().sum()---------------------------")
print(ndf.isnull().sum())

print("-------------------fillna()---------------------------")
ndf["Salary"]=ndf["Salary"].fillna(0)
print(ndf)