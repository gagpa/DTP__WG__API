from typing import List

from app import models as m
from app.db import Session
from app.schemas import general_info as info_sch


class GeneralInfo:

    def get(self) -> info_sch.GeneralInfo:
        return info_sch.GeneralInfo(wg_statuses=self.get_statuses(),
                                    responsible=self.get_responsible(),
                                    wg_types=self.get_wg_types(),
                                    shape_types=self.get_shape_types(),
                                    )

    def get_statuses(self) -> List[info_sch.WgStatusFromDb]:
        s = Session()
        statuses: List[m.WorkGroupStatus] = s.query(m.WorkGroupStatus).all()
        return [info_sch.WgStatusFromDb(id=status.id,
                                        name=status.name,
                                        ) for status in statuses]

    def get_responsible(self) -> List[info_sch.ResponsibleFromDb]:
        s = Session()
        responsible: List[m.Responsible] = s.query(m.Responsible).all()
        return [info_sch.ResponsibleFromDb(id=item.id,
                                           name=item.name
                                           ) for item in responsible]

    def get_wg_types(self) -> List[info_sch.WgTypeFromDb]:
        s = Session()
        types: List[m.WorkGroupType] = s.query(m.WorkGroupType).all()
        return [info_sch.WgTypeFromDb(id=item.id,
                                      name=item.name
                                      ) for item in types]

    def get_shape_types(self) -> List[info_sch.ShapeTypeFromDb]:
        s = Session()
        types: List[m.ShapeType] = s.query(m.ShapeType).all()
        return [info_sch.ShapeTypeFromDb(id=item.id,
                                         name=item.name
                                         ) for item in types]
