from json import dump

from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status
import json
app=FastAPI()

class Employee(BaseModel):
    emp_name: str
    emp_id: int
    emp_city: str

"""
 @app.post(
    '/employee',status_code=status.HTTP_201_CREATED, )
 def insert_emp(employee:Employee):
    print("data is ",employee)
    return {
        "emp_id": employee.emp_id,
        "employee":employee
    }
"""

@app.post('/employee',status_code=status.HTTP_201_CREATED)
def insert_emp(employee:Employee):
    print("data is ", employee)  # pydantic data cant directly convert to json so error happen in file handling
    emp_list=[]
    # 1. Convert the Pydantic model to a standard Python dictionary
    employee_dict = employee.model_dump()  # convert pydantic data to json now u can put in file handle
    try:
        with open("../data.json", "w") as file:
            json.dump(employee_dict, file,indent=3)
            emp_list=emp_list.append(employee_dict)
            # json.dump(employee.emp_id,employee,file)
        return {
            "emp_id": employee.emp_id,
            "employee": employee_dict
        }
    except Exception as e:
        # Convert exception to string so FastAPI can return it safely
        print("error =>  ",str(e))
        return {
            "error":e
        }
@app.get("/emp-data")
def read_emp():
    try:
        with open("../data.json", "r") as file:
            list_data = json.load(file)
            return list_data
    except FileNotFoundError as fe:
        return {
            "file - error": "data.json file not found yet. Insert an employee first."
        }
    except Exception as e:
        return {
            "exception - error": str(e)
        }