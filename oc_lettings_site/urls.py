"""
URLs for oc_lettings_site application
"""

from django.contrib import admin
from django.urls import path, include
from . import views


def trigger_error(request):
    """
    Generate a ZeroDivisionError to ckeck Sentry

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        nothing

    """

    1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]

handler404 = 'oc_lettings_site.views.custom_page_not_found_view'
