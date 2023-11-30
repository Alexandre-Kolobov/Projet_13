"""
ASGI configuration for the Django project.

This module sets up the ASGI (Asynchronous Server Gateway Interface)
application for the Django project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()
