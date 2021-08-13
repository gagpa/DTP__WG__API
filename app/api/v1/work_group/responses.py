from typing import List

from pydantic import BaseModel

from app.api.extenstions.response import SuccessResponse
from app.schemas.work_group import WorkGroupGeoFromDB, WorkGroupFromDb, WorkGroupDelete, WorkGroupFilter


#
# Data
#
class WorkGroupsData(BaseModel):
    work_groups: List[WorkGroupGeoFromDB]


class WorkGroupData(BaseModel):
    work_group: WorkGroupFromDb


class WorkGroupDeleteData(BaseModel):
    work_group: WorkGroupDelete
    message: str = 'Work group was delete'


class WorkGroupsDefaultFilterData(WorkGroupsData):
    config: WorkGroupFilter


#
# Responses
#
class WorkGroupsResponse(SuccessResponse):
    data: WorkGroupsData


class WorkGroupResponse(SuccessResponse):
    data: WorkGroupData


class WorkGroupDeleteResponse(SuccessResponse):
    data: WorkGroupDeleteData


class WorkGroupsDefaultFilterResponse(SuccessResponse):
    data: WorkGroupsDefaultFilterData
