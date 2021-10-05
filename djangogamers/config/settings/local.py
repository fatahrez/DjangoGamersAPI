from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)
SECRET_KEY = env('SECRET_KEY', default='kjb-gx8^h7lgo=4ywlldx7dud6jba-@+cava#=hg9^37d!vs#n')
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
CSRF_TRUSTED_ORIGINS = ['*']
CSRF_COOKIE_SECURE = False
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

CORS_ALLOW_ALL_ORIGINS = True  # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

EDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
