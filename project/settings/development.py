from .base import *  # NOQA

ALLOWED_HOSTS = ['vladislav111.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# --------------------------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
