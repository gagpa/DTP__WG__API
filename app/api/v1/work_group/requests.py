from app.schemas.work_group import WorkGroupToDB, WorkGroupDelete, WorkGroupFilter
from datetime import datetime

class WorkGroupRequest(WorkGroupToDB):
    class Config:
        schema_extra = {'example':
            {
                'type': 1,
                'status': 1,
                'responsible': 1,
                'description': 'Repair road',
                'start_protocol': '2021-07-01',
                'end_protocol': '2021-10-01',
                'start_realization': '2021-07-01',
                'end_realization': '2021-10-01',
                'shapes': [
                    {
                        'type': 'Polygon',
                        'name': 'Crossroad',
                        'coordinates': [[15.5353, 45.4434], [15.5253, 45.4436], [15.5353, 45.4434]],
                        'color': '819FF7',
                        'width': 1,
                        'border_color': '000000',
                        'border_width': 1,
                        'opacity': 1,
                    },
                    {
                        'type': 'Point',
                        'name': 'Crossroad',
                        'coordinates': [[15.5353, 45.4434], [15.5253, 45.4436], [15.5353, 45.4434]],
                        'color': 'DF0174',
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
        end_date = now.strftime('%Y-%m-%d')
        schema_extra = {'example': {
            'type': ['all'],
            'status': ['all'],
            'responsible': ['all'],
            'start_protocol': [start_date, end_date],
            'end_protocol': [start_date, end_date],
            'start_realization': [start_date, end_date],
            'end_realization': [start_date, end_date],
        }
        }

    @classmethod
    def default(cls):
        now = datetime.now()
        start_date = f'{now.year}-01-01'
        end_date = now.strftime('%Y-%m-%d')
        return cls(type=['all'],
                   status=['all'],
                   responsible=['all'],
                   start_protocol=[start_date, end_date],
                   end_protocol=[start_date, end_date],
                   start_realization=[start_date, end_date],
                   end_realization=[start_date, end_date],
                   )


def wg_delete(pk: int) -> WorkGroupDelete:
    return WorkGroupDelete(id=pk)
