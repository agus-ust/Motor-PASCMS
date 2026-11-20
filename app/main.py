from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import POLICY_SOURCE, ROLES

SHARED = Path(__file__).resolve().parent.parent / "shared"
app = FastAPI(title="Motor PAS + CMS (prototype)")
app.mount("/static", StaticFiles(directory=SHARED / "static"), name="static")
templates = Jinja2Templates(directory=str(SHARED / "templates"))


@app.get("/health")
def health():
    return {"status": "ok", "policy_source": POLICY_SOURCE, "roles": ROLES}


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"role": None, "roles": ROLES})
