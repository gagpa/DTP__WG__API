from pydantic import BaseModel


class SuccessResponse(BaseModel):
    """ Успешный ответ """
    success: bool = True
    data: dict


class ErrorResponse(BaseModel):
    """ Ответ об ошибки """
    success: bool = False
    data: dict
