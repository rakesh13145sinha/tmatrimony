from .base import *


SECRET_KEY=env('PRODUCTION_SECRET_KEY')
ALLOWED_HOSTS=[str(host) for host in env('PRODUCTION_ALLOWED_HOSTS').split(",")]

DEBUG=env('PRODUCTION_DEBUG')



# SERVER Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':env('PRO_DB_NAME'),
        'USER': env('PRO_DB_USER'),
        'PASSWORD': env('PRO_DB_PASSWORD'),
        'HOST': env('PRO_DB_HOST'),
        'PORT': env('PRO_DB_PORT')
        }
   
           
}

STATIC_URL='/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static_dir')
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media_dir')


# CSRF_COOKIE_SECURE=True
# SESSION_COOKIE_SECURE=True
# SECURE_SSL_REDIRECT=True
# SECURE_HSTS_SECONDS=True
# SECURE_HSTS_INCLUDE_SUBDOMAINS=True
# SECURE_HSTS_PRELOAD=True



CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOWED_ORIGINS=env('WHITE_LIST', cast=lambda v: [s.strip() for s in v.split(',')])
CORS_ORIGIN_WHITELIST = env('WHITE_LIST', cast=lambda v: [s.strip() for s in v.split(',')])
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = env('WHITE_LIST', cast=lambda v: [s.strip() for s in v.split(',')])
CORS_ALLOW_METHODS = ["DELETE","GET","OPTIONS","PATCH","POST","PUT"]
CORS_ALLOW_HEADERS = ["accept","accept-encoding","authorization","content-type","dnt","origin",
    "user-agent","x-csrftoken","x-requested-with","Jwt"]
