from dotenv import load_dotenv
import os

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", default='9#3be^fspg78v39bd34r2nmh8(^ilg%)rbszl)rx4=w*($jopy')

ALLOWED_HOSTS = []

DEBUG = os.getenv("DJANGO_DEBUG", True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('APPLICATION_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOSTNAME'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

