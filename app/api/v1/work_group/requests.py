from datetime import datetime

from app.schemas.work_group import WorkGroupToDb, WorkGroupDelete, WorkGroupFilter


class WorkGroupRequest(WorkGroupToDb):
    class Config:
        schema_extra = {'example':
            {
                'type': 1,
                'status': 1,
                'responsible': 1,
                'description': 'Repair road',
                'protocol': '2021-07-01',
                'start_realization': '2021-07-01',
                'end_realization': '2021-10-01',
                'shapes': [
                    {
                        'map_id': 'e48a5345d5afe81880721ccc5cea4fe6',
                        'type': 'Polygon',
                        'name': 'Crossroad',
                        'coordinates': [[15.5353, 45.4434], [15.5253, 45.4436], [15.5353, 45.4434]],
                        'color': '819FF7',
                        'width': 1,
                        'border_color': '000000',
                        'border_width': 1,
                        'opacity': 1,
                    }
                ]
            }
        }


class WorkGroupFilterRequest(WorkGroupFilter):
    class Config:
        now = datetime.now()
        start_date = f'{now.year}-01-01'
        end_date = f'{now.year + 1}-01-01'
        schema_extra = {'example': {
            'type': ['all'],
            'status': ['all'],
            'responsible': ['all'],
            'protocol': [start_date, end_date],
            'realization': [start_date, end_date],
        }
        }

    @classmethod
    def default(cls):
        now = datetime.now()
        start_date = f'{now.year}-01-01'
        end_date = f'{now.year + 1}-01-01'
        return cls(type=['all'],
                   status=['all'],
                   responsible=['all'],
                   protocol=[start_date, end_date],
                   realization=[start_date, end_date],
                   )


def wg_delete(pk: int) -> WorkGroupDelete:
    return WorkGroupDelete(id=pk)
