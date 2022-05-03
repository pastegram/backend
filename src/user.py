import os
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends

from deta import Deta

from auth import manager, users
from models import UpdateUser

router = APIRouter()
deta = Deta(os.environ.get("DETA_KEY"))
del_cache = deta.Base("pastegram-deleted")


@router.get("/{username}")
def get_user(username: str):
    user_ = users.get(username)

    if user_ is not None:
        user_["username"] = user_["key"]
        del user_["key"]
        del user_["password"]
        return {"user": user_}

    return {"user": None}


@router.put("/{username}")
def del_user(username: str, new_user: UpdateUser, user=Depends(manager)):
    if user["key"] == username:
        if (user_ := users.get(new_user.username)) is None:
            user_cp = users.get(username)
            user_cp["key"] = new_user.username
            user_cp["email"] = new_user.email
            users.insert(user_cp)
            users.delete(username)
            return {"msg": "Updated user"}
        return {"error": "Username already taken!"}
    return {"error": "Authenticated as different user!"}


@router.delete("/{username}")
def del_user(username: str, user=Depends(manager)):
    if user["key"] == username:
        if (user_ := users.get(username)) is not None:
            del_cache.put(user_, expire_at=datetime.now() + timedelta(days=30))
            users.delete(username)
            return {"msg": "Moved to Delete Trash"}
        return {"error": "User does not exist!"}
    return {"error": "Authenticated as different user!"}