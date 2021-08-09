import os
from datetime import timedelta
# Время жизни токена
ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 1440)))

# Секретный ключ для работы с JWT
JWT_KEY = os.environ.get('SECRET_KEY')

# Алгоритм шифрования
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')
