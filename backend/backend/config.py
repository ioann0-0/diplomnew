import os

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.getenv("DB_NAME", "AttendanceDB"),  # Название БД
        'USER': os.getenv("DB_USER", "sa"),  # Логин
        'PASSWORD': os.getenv("DB_PASSWORD", "your_strong_password"),  # Пароль
        'HOST': os.getenv("DB_HOST", "localhost"),  # Адрес сервера
        'PORT': os.getenv("DB_PORT", "1433"),  # Порт (по умолчанию 1433)
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Название драйвера
        },
    }
}

