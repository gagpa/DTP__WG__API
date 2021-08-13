from fastapi import FastAPI

from app.api.v1 import work_group_router, general_info_router
from .error_handlers import exception_handlers

api = FastAPI(title='WorkGroup API',
              description='WorkGroup Layer API',
              version='1.0',
              exception_handlers=exception_handlers
              )

api.include_router(work_group_router, prefix='/api/v1')
api.include_router(general_info_router, prefix='/api/v1')
