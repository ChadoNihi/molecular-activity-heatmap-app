from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from routers import root
from routers.api import activity

app = FastAPI()

app.mount("/s", StaticFiles(directory="../frontend/public/"), name="static")

app.include_router(root.router)
app.include_router(activity.router)
