import json

student={
    "name":"anubhav",
    "age":22,
    "mobile_number":2015634789
}

print("type of student is::",type((student)))
student_data=json.dumps(student,indent=3,sort_keys=True)
print(student_data)
print("------------------------------------")
print("type of student_ data json  is::",type(student_data))