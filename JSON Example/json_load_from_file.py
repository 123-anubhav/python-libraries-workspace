import json

students=[{
    "name":"anubhav",
    "age":22,
    "mobile_number":2015634789
},
{
    "name":"aashi kumari",
    "age":25,
    "mobile_number":2015634778
}
]
student_data=json.dumps(students,indent=3,sort_keys=True)
print(student_data)
print("------------------------------------")

try:
    with open("student.json", "w") as file:
        json.dump(students,file ,sort_keys=True,indent=3)
except Exception as e:
    print(e)

try:
    with open("student.json", "r") as file:
      print(json.load(file))
except Exception as e:
    print(e)
