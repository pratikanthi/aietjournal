import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aiet.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
