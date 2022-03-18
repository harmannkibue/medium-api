import environ

env = environ.Env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default='9#3be^fspg78v39bd34r2nmh8(^ilg%)rbszl)rx4=w*($jopy')

ALLOWED_HOSTS = []

DEBUG = env.bool("DJANGO_DEBUG", True)
