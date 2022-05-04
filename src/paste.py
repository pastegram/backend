import os
import uuid

from fastapi import APIRouter, Depends

from deta import Deta

from guesslang import Guess

from models import Paste
from auth import manager

router = APIRouter()
deta = Deta(os.environ.get("DETA_KEY"))
pastes = deta.Base("pastegram-pastes")

LANGS = ["Assembly", "Batchfile", "C", "C#", "C++", "Clojure", "CMake", "COBOL", "CoffeeScript", "CSS", "CSV", "Dart",
         "DM", "Dockerfile", "Elixir", "Erlang", "Fortran", "Go", "Groovy", "Haskell", "HTML", "INI", "Java",
         "JavaScript", "JSON", "Julia", "Kotlin", "Lisp", "Lua", "Makefile", "Markdown", "Matlab", "Objective-C",
         "OCaml", "Pascal", "Perl", "PHP", "PowerShell", "Prolog", "Python", "R", "Ruby", "Rust", "Scala", "Shell",
         "SQL", "Swift", "TeX", "TOML", "TypeScript", "Verilog", "Visual Basic", "XML", "YAML", "Other"]


@router.post("/paste")
def new_paste(paste: Paste, user=Depends(manager)):
    if paste.content in [None, ""]:
        return {"error": "Content cannot be empty"}

    if paste.language not in ["", "Auto", "Auto Detect", "Auto-detect", "Auto-Detect", "auto-detect"] and paste.language not in LANGS:
        return {"error": "Unknown Language"}

    lang = Guess().language_name(paste.content) if paste.language in ["", "Auto", "Auto Detect", "Auto-detect", "Auto-Detect", "auto-detect"] else paste.language
    pid = str(uuid.uuid4())

    if pastes.fetch({"filename": paste.filename, "username": user["key"]}).items not in [[], {}, None]:
        return {"error": "Filename already in use"}

    pastes.insert(
        {
            "username": user["key"],
            "filename": paste.filename,
            "language": lang,
            "content": paste.content
        },
        pid
    )
    return {"pid": pid, "language": lang}


@router.get("/users/{username}/pastes")
def get_pastes(username: str):
    if pastes.fetch({"username": username}).items in [None, {}]:
        return {"error": "User does not exist!"}

    return {"pastes": pastes.fetch({"username": username}).items}


@router.get("/users/{username}/{filename}")
def get_paste(username: str, filename: str):
    try:
        return {"paste": pastes.fetch({"username": username, "filename": filename}).items[0]}
    except IndexError:
        return {"error": "Paste does not exist!"}


@router.delete("/users/{username}/{filename}")
def delete_paste(username: str, filename: str, user=Depends(manager)):
    if user["key"] != username:
        return {"error": "Authenticated as different user!"}

    if (paste := pastes.fetch({"filename": filename, "username": username}).items) not in [[], {}, None]:
        pastes.delete(paste[0]["key"])
        return {"success": True}
    else:
        print(paste)
        return {"error": "Filename doesnt exist"}
