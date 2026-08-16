from pydantic import BaseModel, Field


class UserDto(BaseModel):
    #userid: int
    username: str =Field(min_length=3,max_length=20)  #Field is use for validate input just like hibernate validator in java
    city:str
    mobile:str = Field(min_length=6,max_length=20)