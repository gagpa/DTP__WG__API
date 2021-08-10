from typing import List

from pydantic import BaseModel


class WgStatusFromDb(BaseModel):
    id: int
    name: str


class ResponsibleFromDb(BaseModel):
    id: int
    name: str


class WgTypeFromDb(BaseModel):
    id: int
    name: str


class ShapeTypeFromDb(BaseModel):
    id: int
    name: str


class GeneralInfo(BaseModel):
    wg_statuses: List[WgStatusFromDb]
    responsible: List[ResponsibleFromDb]
    wg_types: List[WgTypeFromDb]
    shape_types: List[ShapeTypeFromDb]
