from fastapi import APIRouter, Depends

from app.components.shape import ShapeComponent
from . import requests as rq
from . import responses as rs

router = APIRouter(tags=['Shape'], prefix='/shape')


@router.get('/{pk}',
            response_model=rs.ShapeResponse,
            description='Read by pk'
            )
async def read(pk: int):
    """Read shape data by pk"""
    shape = ShapeComponent().read(pk)
    return rs.ShapeResponse(data=rs.ReadShapeData(shape=shape))
