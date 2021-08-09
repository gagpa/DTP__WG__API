from pydantic import BaseModel

from app.api.extenstions.response import SuccessResponse
from app.schemas.shape import ShapeData


#
# Data
#

class ReadShapeData(BaseModel):
    shape: ShapeData


#
# Responses
#
class ShapeResponse(SuccessResponse):
    data: ReadShapeData
