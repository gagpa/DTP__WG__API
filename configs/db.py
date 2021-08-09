import os


class DbEnvNotFound(KeyError):
    pass


DRIVER = 'postgresql+psycopg2'
try:
    HOST = os.environ['DB_HOST']
    PORT = os.environ['DB_PORT']
    USER = os.environ['DB_USER']
    PASS = os.environ['DB_PASS']
    NAME = os.environ['DB_NAME']
except KeyError:
    raise DbEnvNotFound

URL = f'{DRIVER}://{USER}:{PASS}@{HOST}/{NAME}'
