import uvicorn

from app.api import api
from seed.seed import seed


def main():
    """ Запуск """
    seed()
    uvicorn.run(api, host='0.0.0.0')


if __name__ == '__main__':
    main()
