from .general import ValidationError, pydantic_validation, RequestValidationError, request_validation, unexpected

exception_handlers = {

    # general
    RequestValidationError: request_validation,
    # ValidationError: pydantic_validation,
    # Exception: unexpected,
}
