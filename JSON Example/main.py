from fastapi import FastAPI

app=FastAPI()

@app.get("/welcome")
def welcome_msg():
    return{"message":"welcome to welcome_msg"}

@app.get("/greet")
def greet_msg():
    return{"message":"welcome to greet_msg"}
