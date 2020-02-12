from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from routers import root

app = FastAPI()

app.mount("/s", StaticFiles(directory="../frontend/public/"), name="static")

app.include_router(root.router)
