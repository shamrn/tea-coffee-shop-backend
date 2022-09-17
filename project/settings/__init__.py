import os

configuration = os.environ.get('SETTINGS_CONFIGURATION')

if configuration == 'local':
    from .local import *
elif configuration == 'development':
    from .development import *
else:
    from .base import *
