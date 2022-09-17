from .base import *  # NOQA

# General
# --------------------------------------------------------------------------------------------------
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS.append('debug_toolbar', )

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware', )

# Debug toolbar
# --------------------------------------------------------------------------------------------------
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}
