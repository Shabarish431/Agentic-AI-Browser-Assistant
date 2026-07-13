from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    resume_text: str

class Command(BaseModel):
    command: str