from enum import Enum
from typing import List, Union

from pydantic import BaseModel, Field

from app import models as m
from app.db import Session


class TypeGeometry(Enum):
    """Тип формы события"""
    point = 'Point'
    polygon = 'Polygon'
    line = 'LineString'


class Shape(BaseModel):
    """Элемент события"""
    type: TypeGeometry
    name: str
    coordinates: Union[List[List[float]], List[float]]
    color: str
    width: int
    border_color: str
    border_width: int
    opacity: int = Field(..., ge=0, le=1)


class ShapeFromDb(Shape):
    id: int

    class Config:
        orm_mode = True

    @classmethod
    def by_orm(cls, model: m.Shape):
        return cls(id=model.id,
                   type=model.shape_type.name,
                   name=model.name,
                   coordinates=model.coordinates,
                   color=model.color,
                   width=model.width,
                   border_color=model.border_color,
                   border_width=model.border_width,
                   opacity=model.opacity
                   )

    def update(self):
        shape: m.Shape = Session().query(m.Shape).get(self.id)
        shape.shape_type_id = self.type
        shape.name = self.name
        shape.coordinates = self.coordinates
        shape.color = self.color
        shape.width = self.width
        shape.border_color = self.border_color
        shape.border_width = self.border_width
        shape.opacity = self.opacity
        Session().commit()
        return self


class ShapeToDb(Shape):
    type: int

    def insert(self, wg_pk: int) -> ShapeFromDb:
        """Insert data in DB"""
        s = Session()
        shape = m.Shape(name=self.name,
                        color=self.color,
                        width=self.width,
                        border_width=self.border_width,
                        border_color=self.border_color,
                        coordinates=self.coordinates,
                        opacity=self.opacity,
                        shape_type_id=self.type,
                        work_group_id=wg_pk
                        )
        s.add(shape)
        s.commit()
        shape = ShapeFromDb(id=shape.id,
                            type=shape.shape_type.name,
                            name=shape.name,
                            coordinates=shape.coordinates,
                            color=shape.color,
                            width=shape.width,
                            border_color=shape.border_color,
                            border_width=shape.border_width,
                            opacity=shape.opacity
                            )
        return shape

    def update(self, pk: int, is_update: bool = True) -> ShapeFromDb:
        if is_update:
            shape = Session().query(m.Shape).get(pk)
        else:
            shape = m.Shape()
            shape.work_group_id = pk
        shape.shape_type_id = self.type
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
                           type=shape.shape_type.name,
                           name=shape.name,
                           coordinates=shape.coordinates,
                           color=shape.color,
                           width=shape.width,
                           border_color=shape.border_color,
                           border_width=shape.border_width,
                           opacity=shape.opacity
                           )


class ShapeData(BaseModel):
    id: str
    name: str
    type: str

    @classmethod
    def by_pk(cls, pk):
        shape = Session().query(m.Shape).get(pk)
        return cls(id=shape.id,
                   name=shape.name,
                   type=shape.shape_type.name)
