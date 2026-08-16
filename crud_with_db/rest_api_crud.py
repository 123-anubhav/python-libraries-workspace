from contextlib import asynccontextmanager

from fastapi import FastAPI
import user_dto
import DB as user_db


#app = FastAPI()

"""   -----------------     DEPRECATED  ----------------
@app.on_event("startup")
def startup():
    user_db.create_tables()
 
"""

# 1. Define the lifespan function
@asynccontextmanager
async def lifespan(app: FastAPI): # STARTUP METHOD RECOMMENDED TO NAME AS lifespan
    # This runs on startup
    user_db.create_tables()
    yield  # The app runs while paused here
    # Optional: Put shutdown/cleanup logic here if needed
# 2. Pass the lifespan to the FastAPI instance
app = FastAPI(lifespan=lifespan)

@app.get("/users")
def get_all_users():
    return user_db.get_all_users()
@app.post("/user")
def create_user(user: user_dto.UserDto):
    return user_db.insert_user(user)