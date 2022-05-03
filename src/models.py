from pydantic import BaseModel


class RegisterUser(BaseModel):
    username: str
    email: str
    password: str


class LoginUser(BaseModel):
    username: str
    password: str


class UpdateUser(BaseModel):
    username: str
    email: str
