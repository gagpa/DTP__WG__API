from datetime import date
from pydantic import BaseModel
from typing import List, Union

from app import models as m
from app.db import Session
from .shape import ShapeToDb, ShapeFromDb


class WorkGroupDelete(BaseModel):
    """"""
    id: int

    def delete(self):
        s = Session()
        wg = s.query(m.WorkGroup).get(self.id)
        s.delete(wg)
        s.commit()
        s.close()


class WorkGroupGeoFromDB(BaseModel):
    id: int
    shapes: List[ShapeFromDb]

    class Config:
        orm_mode = True

    @classmethod
    def get_all(cls):
        s = Session()
        query = s.query(m.WorkGroup)
        wgs = [cls(id=wg.id,
                   shapes=[ShapeFromDb.by_orm(shape) for shape in wg.shapes]
                   ) for wg in query.all()]
        s.close()
        return wgs


class WorkGroupFromDb(BaseModel):
    """WorkGroup from DB"""
    id: int
    type: int
    status: int
    responsible: int
    description: str
    shapes: List[ShapeFromDb]
    end_realization: date
    protocol: date
    start_realization: date

    class Config:
        orm_mode = True

    @classmethod
    def by_pk(cls, pk: int):
        s = Session()
        query = s.query(m.WorkGroup).filter_by(id=pk)
        wg = query.one()
        wg = cls(id=wg.id,
                 type=wg.type.id,
                 status=wg.status.id,
                 responsible=wg.responsible.id,
                 description=wg.description,
                 protocol=wg.protocol,
                 start_realization=wg.start_realization,
                 end_realization=wg.end_realization,
                 shapes=[ShapeFromDb(id=item.id,
                                     map_id=item.map_id,
                                     type=item.shape_type.name,
                                     name=item.name,
                                     coordinates=item.coordinates,
                                     color=item.color,
                                     width=item.width,
                                     border_color=item.color,
                                     border_width=item.border_width,
                                     opacity=item.opacity,
                                     ) for item in wg.shapes]
                 )
        s.close()
        return wg


class WorkGroupToDb(BaseModel):
    description: str
    end_realization: date
    responsible: int
    shapes: List[ShapeToDb]
    protocol: date
    start_realization: date
    status: int
    type: int

    def insert(self) -> WorkGroupFromDb:
        s = Session()
        wg = m.WorkGroup(description=self.description,
                         protocol=self.protocol,
                         start_realization=self.start_realization,
                         end_realization=self.end_realization,
                         type_id=self.type,
                         status_id=self.status,
                         responsible_id=self.responsible,
                         )
        s.add(wg)
        s.commit()
        shapes = [shape.insert(wg.id) for shape in self.shapes]

        wg = WorkGroupFromDb(id=wg.id,
                             type=wg.type.id,
                             status=wg.status.id,
                             responsible=wg.responsible.id,
                             description=wg.description,
                             protocol=wg.protocol,
                             start_realization=wg.start_realization,
                             end_realization=wg.end_realization,
                             shapes=shapes)
        s.close()
        return wg

    def update(self, pk) -> WorkGroupFromDb:
        wg = Session().query(m.WorkGroup).get(pk)
        wg.type_id = self.type
        wg.status_id = self.status
        wg.responsible_id = self.responsible
        wg.description = self.description
        wg.protocol = self.protocol
        wg.start_realization = self.start_realization
        wg.end_realization = self.end_realization
        Session().commit()
        wg = Session().query(m.WorkGroup).get(pk)
        new_shape_ids = {str(shape.map_id) for shape in self.shapes}

        for shape in tuple(filter(lambda shape: str(shape.id) not in new_shape_ids, wg.shapes)):
            Session.delete(shape)
        Session().commit()
        wg = Session().query(m.WorkGroup).get(pk)
        shape_ids = {str(shape.id) for shape in wg.shapes}

        for shape in self.shapes:
            if shape.map_id in shape_ids:
                shape.update()
            else:
                shape.insert(pk)
        Session().commit()

        return WorkGroupFromDb.by_pk(pk)


class WorkGroupFilter(BaseModel):
    type: List[Union[int, str]] = ['all']
    status: List[Union[int, str]] = ['all']
    responsible: List[Union[int, str]] = ['all']
    protocol: List[date]
    realization: List[date]

    def filter(self) -> List[WorkGroupGeoFromDB]:
        s = Session()
        filter_obj = []
        if self.type != ['all']:
            filter_obj.append(m.WorkGroup.type_id.in_(self.type))
        if self.status != ['all']:
            filter_obj.append(m.WorkGroup.status_id.in_(self.status))
        if self.responsible != ['all']:
            filter_obj.append(m.WorkGroup.responsible_id.in_(self.responsible))
        filter_obj.append(m.WorkGroup.protocol.between(*self.protocol))
        filter_obj.append(m.WorkGroup.start_realization >= self.realization[0])
        filter_obj.append(m.WorkGroup.end_realization <= self.realization[1])
        query = s.query(m.WorkGroup).filter(*filter_obj)
        wgs = [WorkGroupGeoFromDB(id=wg.id,
                                  shapes=[ShapeFromDb.by_orm(shape) for shape in wg.shapes]
                                  ) for wg in query.all()]
        s.close()
        return wgs
