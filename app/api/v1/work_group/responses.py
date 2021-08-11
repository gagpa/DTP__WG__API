from typing import List

from pydantic import BaseModel

from app.api.extenstions.response import SuccessResponse
from app.schemas.work_group import WorkGroupShortFromDB, WorkGroupDataFromDB, WorkGroupDelete, WorkGroupFilter


#
# Data
#
class WorkGroupsData(BaseModel):
    work_groups: List[WorkGroupShortFromDB]


class WorkGroupData(BaseModel):
    work_group: WorkGroupDataFromDB


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
