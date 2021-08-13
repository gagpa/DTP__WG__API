from enum import Enum
from typing import List, Union, Optional

from pydantic import BaseModel, Field

from app import models as m
from app.db import Session


class TypeGeometry(Enum):
    """Тип формы события"""
    point = 'Point'
    polygon = 'Polygon'
    line = 'LineString'


class ShapeFromDb(BaseModel):
    id: int
    map_id: str
    name: str
    type: TypeGeometry
    coordinates: Union[List[List[List[float]]], List[List[float]], List[float]]
    color: str
    width: int
    border_color: str
    border_width: int
    opacity: float = Field(..., ge=0, le=1)

    class Config:
        orm_mode = True

    @classmethod
    def by_orm(cls, model: m.Shape):
        return cls(id=model.id,
                   map_id=model.map_id,
                   type=model.shape_type.name,
                   name=model.name,
                   coordinates=model.coordinates,
                   color=model.color,
                   width=model.width,
                   border_color=model.border_color,
                   border_width=model.border_width,
                   opacity=model.opacity
                   )


class ShapeToDb(BaseModel):
    map_id: Optional[str] = None
    type: TypeGeometry
    name: str
    coordinates: Union[List[List[List[float]]], List[List[float]], List[float]]
    color: str
    width: int
    border_color: str
    border_width: int
    opacity: float = Field(..., ge=0, le=1)

    def insert(self, wg_pk: int) -> ShapeFromDb:
        """Insert data in DB"""
        s = Session()
        shape_type = s.query(m.ShapeType).filter_by(name=self.type.value).one()
        shape = m.Shape(map_id=self.map_id,
                        name=self.name,
                        color=self.color,
                        width=self.width,
                        border_width=self.border_width,
                        border_color=self.border_color,
                        coordinates=self.coordinates,
                        opacity=self.opacity,
                        shape_type_id=shape_type.id,
                        work_group_id=wg_pk,
                        )
        s.add(shape)
        s.commit()
        shape = ShapeFromDb(id=shape.id,
                            map_id=shape.map_id,
                            type=shape.shape_type.name,
                            name=shape.name,
                            coordinates=shape.coordinates,
                            color=shape.color,
                            width=shape.width,
                            border_color=shape.border_color,
                            border_width=shape.border_width,
                            opacity=shape.opacity,
                            )
        return shape

    def update(self, pk: str, is_update: bool = True) -> ShapeFromDb:
        if is_update:
            shape = Session().query(m.Shape).get(pk)
        else:
            shape = m.Shape()
            shape.work_group_id = pk
            shape.map_id = self.map_id
        shape_type = Session().query(m.ShapeType).filter_by(name=self.type.value).one()
        shape.shape_type_id = shape_type.id
        shape.name = self.name
        shape.coordinates = self.coordinates
        shape.color = self.color
        shape.width = self.width
        shape.border_color = self.border_color
        shape.border_width = self.border_width
        shape.opacity = self.opacity
        if not is_update:
            Session().add(shape)
        Session().commit()
        return ShapeFromDb(id=shape.id,
                           map_id=shape.map_id,
                           type=shape.shape_type.name,
                           name=shape.name,
                           coordinates=shape.coordinates,
                           color=shape.color,
                           width=shape.width,
                           border_color=shape.border_color,
                           border_width=shape.border_width,
                           opacity=shape.opacity
                           )
