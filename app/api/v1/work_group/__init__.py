from fastapi import APIRouter, Depends

from app.components.work_group import WorkGroupComponent
from . import requests as rq
from . import responses as rs

router = APIRouter(tags=['WorkGroup'], prefix='/work_group')


@router.get('/all',
            response_model=rs.WorkGroupsResponse,
            description='Read all'
            )
async def read_all():
    """Вернуть все рабочии группы"""
    wgs = WorkGroupComponent().read_all()
    return rs.WorkGroupsResponse(data=rs.WorkGroupsData(work_groups=wgs))


@router.get('/{pk}',
            response_model=rs.WorkGroupResponse,
            description='Read by pk'
            )
async def read(pk: int):
    """Вернуть полную информацию о рабочей группе"""
    wg = WorkGroupComponent().read(pk)
    return rs.WorkGroupResponse(data=rs.WorkGroupData(work_group=wg))


@router.post('/',
             response_model=rs.WorkGroupResponse,
             description='Create',
             status_code=201
             )
async def create(wg: rq.WorkGroupRequest):
    """Вернуть создать рабочую группу"""
    wg = WorkGroupComponent().create(wg)
    return rs.WorkGroupResponse(data=rs.WorkGroupData(work_group=wg))


@router.post('/{pk}',
             response_model=rs.WorkGroupResponse,
             description='Update'
             )
async def update(pk: int, wg: rq.WorkGroupRequest):
    """Вернуть обновить рабочую группу"""
    wg = WorkGroupComponent().update(pk, wg)
    return rs.WorkGroupResponse(data=rs.WorkGroupData(work_group=wg))


@router.delete('/{pk}',
               response_model=rs.WorkGroupDeleteResponse,
               description='Delete'
               )
async def delete(wg=Depends(rq.wg_delete)):
    """Вернуть удалить рабочую группу"""
    WorkGroupComponent().delete(wg)
    return rs.WorkGroupDeleteResponse(data=rs.WorkGroupDeleteData(work_group=wg))
