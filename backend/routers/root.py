from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter()


@router.get("/")
async def root():
	# FIXME: make work w/ `await`? see
	# https://www.starlette.io/responses/#fileresponse
    return FileResponse('../frontend/public/index.html', media_type='text/html')
