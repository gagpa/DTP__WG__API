from datetime import date
from typing import List, Union

from pydantic import BaseModel

from app import models as m
from app.db import Session
from .shape import Shape, ShapeToDb, ShapeFromDb


class WorkGroupData(BaseModel):
    """Data of WorkGroup"""
    type: str
    status: str
    responsible: str
    description: str
    start_protocol: date
    end_protocol: date
    start_realization: date
    end_realization: date


class WorkGroupDelete(BaseModel):
    """"""
    id: int

    def delete(self):
        s = Session()
        wg = s.query(m.WorkGroup).get(self.id)
        s.delete(wg)
        s.commit()
        s.close()


class WorkGroup(WorkGroupData):
    """Full data of WorkGroup"""
    shapes: List[Shape]


class WorkGroupShort(BaseModel):
    """Short data of WorkGroup"""
    shapes: List[Shape]


class WorkGroupShortFromDB(WorkGroupShort):
    id: str
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


class WorkGroupFromDB(WorkGroup):
    """WorkGroup from DB"""
    id: str

    class Config:
        orm_mode = True


class WorkGroupDataFromDB(WorkGroupData):
    """WorkGroup from DB"""
    id: str

    class Config:
        orm_mode = True

    @classmethod
    def by_pk(cls, pk: int):
        s = Session()
        query = s.query(m.WorkGroup).filter_by(id=pk)
        wg = query.one()
        wg = cls(id=wg.id,
                 type=wg.type.name,
                 status=wg.status.name,
                 responsible=wg.responsible.name,
                 description=wg.description,
                 start_protocol=wg.start_protocol,
                 end_protocol=wg.end_protocol,
                 start_realization=wg.start_realization,
                 end_realization=wg.end_realization,
                 )
        s.close()
        return wg


class WorkGroupToDB(WorkGroup):
    type: int
    status: int
    responsible: int
    shapes: List[ShapeToDb]

    def insert(self) -> WorkGroupFromDB:
        s = Session()
        wg = m.WorkGroup(description=self.description,
                         start_protocol=self.start_protocol,
                         end_protocol=self.end_protocol,
                         start_realization=self.start_realization,
                         end_realization=self.end_realization,
                         type_id=self.type,
                         status_id=self.status,
                         responsible_id=self.responsible,
                         )
        s.add(wg)
        s.commit()
        shapes = [shape.insert(wg.id) for shape in self.shapes]

        wg = WorkGroupFromDB(id=wg.id,
                             type=wg.type.name,
                             status=wg.status.name,
                             responsible=wg.responsible.name,
                             description=wg.description,
                             start_protocol=wg.start_protocol,
                             end_protocol=wg.end_protocol,
                             start_realization=wg.start_realization,
                             end_realization=wg.end_realization,
                             shapes=shapes)
        s.close()
        return wg

    def update(self, pk) -> WorkGroupFromDB:
        wg = Session().query(m.WorkGroup).get(pk)
        wg.type_id = self.type
        wg.status_id = self.status
        wg.responsible_id = self.responsible
        wg.description = self.description
        wg.start_protocol = self.start_protocol
        wg.end_protocol = self.end_protocol
        wg.start_realization = self.start_realization
        wg.end_realization = self.end_realization
        Session().commit()
        shapes = []
        if len(self.shapes) < len(wg.shapes):
            for item in wg.shapes[:len(self.shapes) + 1]:
                Session.delete(item)
        Session().commit()
        for i, shape in enumerate(self.shapes):
            if i + 1 < len(wg.shapes):
                updated_shape = shape.update(wg.shapes[i].id, is_update=True)
            else:
                updated_shape = shape.update(wg.id, is_update=False)
            shapes.append(updated_shape)
        wg = WorkGroupFromDB(id=wg.id,
                             type=wg.type.name,
                             status=wg.status.name,
                             responsible=wg.responsible.name,
                             description=wg.description,
                             start_protocol=wg.start_protocol,
                             end_protocol=wg.end_protocol,
                             start_realization=wg.start_realization,
                             end_realization=wg.end_realization,
                             shapes=shapes)
        return wg


class WorkGroupFilter(BaseModel):
    type: List[Union[int, str]] = ['all']
    status: List[Union[int, str]] = ['all']
    responsible: List[Union[int, str]] = ['all']
    start_protocol: List[date]
    end_protocol: List[date]
    start_realization: List[date]
    end_realization: List[date]

    def filter(self) -> List[WorkGroupShortFromDB]:
        s = Session()
        filter_obj = []
        if self.type != ['all']:
            filter_obj.append(m.WorkGroup.type_id.in_(self.type))
        if self.status != ['all']:
            filter_obj.append(m.WorkGroup.status_id.in_(self.status))
        if self.responsible != ['all']:
            filter_obj.append(m.WorkGroup.responsible_id.in_(self.responsible))
        filter_obj.append(m.WorkGroup.start_protocol.between(*self.start_protocol))
        filter_obj.append(m.WorkGroup.end_protocol.between(*self.end_protocol))
        filter_obj.append(m.WorkGroup.start_realization.between(*self.start_realization))
        filter_obj.append(m.WorkGroup.end_realization.between(*self.end_realization))
        query = s.query(m.WorkGroup).filter(*filter_obj)
        wgs = [WorkGroupShortFromDB(id=wg.id,
                                    shapes=[ShapeFromDb.by_orm(shape) for shape in wg.shapes]
                                    ) for wg in query.all()]
        s.close()
        return wgs
