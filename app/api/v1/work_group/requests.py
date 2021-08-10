from app.schemas.work_group import WorkGroupToDB, WorkGroupDelete


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


def wg_delete(pk: int) -> WorkGroupDelete:
    return WorkGroupDelete(id=pk)
