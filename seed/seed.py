import json

from app.models import ShapeType, Responsible, WorkGroupStatus, WorkGroupType
from app.db import Session

seed_translate = {'wg_statuses': WorkGroupStatus,
                  'wg_types': WorkGroupType,
                  'shape_types': ShapeType,
                  'responsible': Responsible}


def seed():
    with open('seed/seed.json') as file:
        data = json.load(file)
    s = Session()
    for key, value in data.items():
        Model = seed_translate[key]
        for v in value:
            if not s.query(s.query(Model).filter_by(**v).exists()).scalar():
                model = Model(**v)
                s.add(model)
    s.commit()
    s.close()
