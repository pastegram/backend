from pydantic import BaseModel
import uuid


class RegisterUser(BaseModel):
    """
    Model for new user registration
    """
    username: str
    email: str
    password: str


class LoginUser(BaseModel):
    """
    Model for authorization of pre-existing users
    """
    username: str
    password: str


class UpdateUser(BaseModel):
    """
    Model for updating existing users' data
    """
    username: str
    email: str


class Paste(BaseModel):
    """
    Model for pastes
    """
    filename: str = str(uuid.uuid4())
    content: str
    language: str


class TemporaryPaste(BaseModel):
    """
    Model for anonymous pastes
    """
    content: str
    language: str
