from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.api.extenstions.response import ErrorResponse
from configs.app import MODE


def unexpected(request: Request, exc: Exception) -> JSONResponse:
    """ Непредвиденные ошибки """
    if MODE == 'development':
        response = ErrorResponse(data={'message': 'Критическая ошибка',
                                       'exc': repr(exc),
                                       'args': exc.args})
        return JSONResponse(status_code=500,
                            content=jsonable_encoder(response))

    response = ErrorResponse(success=False,
                             data={'message': 'Сервис недоступен'})
    return JSONResponse(status_code=500,
                        content=jsonable_encoder(response))


def request_validation(request: Request, exc: RequestValidationError) -> JSONResponse:
    """ Ошибка валидации переданных данных """
    fields = []
    for field in exc.errors():
        loc: tuple = field['loc']
        msg: str = field['msg']
        error: str = field['type']
        fields.append({'location': ' - '.join(map(str, loc)),
                       'message': msg,
                       'error': error})
    response = ErrorResponse(success=False,
                             data={'message': 'Ошибка валидации входных данных',
                                   'fields': fields})
    return JSONResponse(status_code=422,
                        content=jsonable_encoder(response))


def pydantic_validation(request: Request, exc: ValidationError) -> JSONResponse:
    """ Ошибка при валидации данных в pydantic схеме """
    response = ErrorResponse(success=False,
                             data={'message': 'Ошибка валидации входных данных'})
    return JSONResponse(status_code=422,
                        content=jsonable_encoder(response))
