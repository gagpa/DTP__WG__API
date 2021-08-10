from fastapi import APIRouter

from app.components.general_info import GeneralInfo
from app.schemas import general_info as info_sch
from . import requests as rq
from . import responses as rs

router = APIRouter(tags=['General Info'], prefix='/general-info')


@router.get('/',
            response_model=rs.GeneralInfoResponse,
            description='Read all general info of current API'
            )
async def read():
    """Read GeneralInfo"""
    general_info: info_sch.GeneralInfo = GeneralInfo().get()
    return rs.GeneralInfoResponse(data=general_info)
