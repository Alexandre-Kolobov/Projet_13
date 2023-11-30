"""
WSGI configuration for the Django project.

This module sets up the WSGI (Web Server Gateway Interface) application for the Django project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()
