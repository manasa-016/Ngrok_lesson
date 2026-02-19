from pydantic import BaseModel

class UserSchema(BaseModel):
    email:str
    password:str
    
class UserUpdateApikey(BaseModel):
    api_key:str