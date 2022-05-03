import os

from fastapi import APIRouter, Depends
from fastapi.responses import Response
from fastapi_login import LoginManager

from dotenv import load_dotenv

from deta import Deta

import bcrypt

from models import RegisterUser, LoginUser

load_dotenv()

router = APIRouter()
manager = LoginManager(os.environ.get("SECRET"), "/login")
deta = Deta(os.environ.get("DETA_KEY"))
users = deta.Base("pastegram-users")


@manager.user_loader()
def query_user(username: str):
    return users.get(username)


@router.post("/register")
def register(user: RegisterUser, response: Response):
    '''
    Register new user
    '''
    exists = True if query_user(user.username) is not None else False

    if exists:
        return {"error": "Username already exists!"}

    try:
        hpw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        users.insert({"email": user.email, "password": hpw.decode()}, user.username)
        access_token = manager.create_access_token(data={"sub": user.username})
        manager.set_cookie(response, access_token)
        return {"success": True, "msg": "Successfully created user!", "token": access_token}
    except Exception as e:
        return {"error": "An Unknown error occurred!", "exception": str(e)}


@router.post("/login")
def login(user: LoginUser, response: Response):
    '''
    Login to an existing account
    '''
    exists = True if (user_ := query_user(user.username)) is not None else False

    if not exists:
        return {"error": "User does not exist!"}

    if not bcrypt.checkpw(user.password.encode(), user_["password"].encode()):
        return {"error": "Incorrect password"}

    access_token = manager.create_access_token(data={"sub": user.username})
    manager.set_cookie(response, access_token)
    return {"token": access_token}
