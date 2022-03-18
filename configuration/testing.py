from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'schoole_system_db_main',
        'USER': 'kirill',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': 5432,
    }
}
