from app.api.extenstions.response import SuccessResponse
from app.schemas.general_info import GeneralInfo


class GeneralInfoResponse(SuccessResponse):
    data: GeneralInfo
