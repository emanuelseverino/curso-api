PROJETO BASE PARA UM PROJETO DJANGO

1º Faça o clone do projeto

2º Instale a Venv:
    - python -m venv venv

3º Criar o arquivo "projeto/local_settings.py" com essas configurações:
    
    from projeto.settings import BASE_DIR

    SECRET_KEY = 'django-insecure-nagj+$4d&1wg4rm(g0dt4ot0ztnterc#34t_=$3et2q^e27979'

    DEBUG = True

    ALLOWED_HOSTS = ['*', ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'mydatabase',
    #         'USER': 'myuser',
    #         'PASSWORD': 'mypassword',
    #         'HOST': 'localhost',
    #         'PORT': '5432',
    #     }
    # }
    
    DEFAULT_FROM_EMAIL = 'Estude API'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST_USER = 'emanuelsmseverino@gmail.com'
    EMAIL_HOST_PASSWORD = 'lbexucwrqlhhrveg'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'

