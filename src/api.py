from fastapi import FastAPI

import auth
import user
import paste
import guest

api = FastAPI(title="Pastegram", version="0.1.0", description="The next generation of pastebin!", debug=True)

api.include_router(auth.router, tags=["auth"], prefix="/auth")
api.include_router(paste.router, tags=["paste"])
api.include_router(guest.router, tags=["paste"])
api.include_router(user.router, tags=["user"])


@api.get("/")
def index():
    return {"ok": True}
