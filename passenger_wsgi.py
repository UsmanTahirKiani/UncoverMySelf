import sys

sys.path.insert(0, "/home/unce3946/app")

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'NiceAdmin.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
