from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter()


@router.get("/api/activity")
async def activity():
	pass
