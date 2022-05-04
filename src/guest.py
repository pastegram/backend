import os
import uuid

from fastapi import APIRouter

from deta import Deta

from guesslang import Guess

from models import TemporaryPaste

router = APIRouter()
deta = Deta(os.environ.get("DETA_KEY"))
pastes = deta.Base("pastegram-guest")

LANGS = ["Assembly", "Batchfile", "C", "C#", "C++", "Clojure", "CMake", "COBOL", "CoffeeScript", "CSS", "CSV", "Dart",
         "DM", "Dockerfile", "Elixir", "Erlang", "Fortran", "Go", "Groovy", "Haskell", "HTML", "INI", "Java",
         "JavaScript", "JSON", "Julia", "Kotlin", "Lisp", "Lua", "Makefile", "Markdown", "Matlab", "Objective-C",
         "OCaml", "Pascal", "Perl", "PHP", "PowerShell", "Prolog", "Python", "R", "Ruby", "Rust", "Scala", "Shell",
         "SQL", "Swift", "TeX", "TOML", "TypeScript", "Verilog", "Visual Basic", "XML", "YAML", "Other"]


@router.get("/paste/{pid}")
def guest_paste(pid: str):
    if pastes.get(pid) is None:
        return {"error": "Either paste does not exist or it has expired!"}
    return {"paste": pastes.get(pid)}


@router.post("/guestpaste")
def guest_paste_create(paste: TemporaryPaste):
    if paste.content in [None, ""]:
        return {"error": "Content cannot be empty"}

    if paste.language not in ["", "Auto", "Auto Detect", "Auto-detect", "Auto-Detect", "auto-detect"] and paste.language not in LANGS:
        return {"error": "Unknown Language"}

    lang = Guess().language_name(paste.content) if paste.language in ["", "Auto", "Auto Detect", "Auto-detect", "Auto-Detect", "auto-detect"] else paste.language
    pid = str(uuid.uuid4())

    pastes.put(
        {
            "language": lang,
            "content": paste.content
        },
        pid,
        expire_in=86400
    )
    return {"pid": pid, "language": lang}
