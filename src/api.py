from fastapi import FastAPI

from auth import auth

api = FastAPI()

api.mount("/auth", auth)


@api.get("/")
def index():
    return {"ok": True}

