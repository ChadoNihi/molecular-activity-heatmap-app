import json
from fastapi import APIRouter
from starlette.responses import FileResponse

ACTIVITY_DATA_JSON = "data/pchembl_values.json"

router = APIRouter()

with open(ACTIVITY_DATA_JSON, "r") as f:
    activity_data = json.load(f)


@router.get("/api/activity")
async def activity():
	return activity_data
