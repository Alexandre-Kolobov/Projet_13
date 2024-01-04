"""
Module containing Django views for the oc_lettings_site app.

Functions:
    index - Render the oc_lettings_site index page
    my_custom_page_not_found_view - Render the oc_lettings_site 404 page
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from sentry_sdk import capture_message


def index(request: HttpRequest) -> HttpResponse:
    """
    Render the oc_lettings_site index page

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The HTTP response containing the rendered oc_lettings_site index page

    """

    return render(request, 'index.html')


def custom_page_not_found_view(request: HttpRequest, exception: Exception = None) -> HttpResponse:
    """
    Render the oc_lettings_site 404 page

    Parameters:
        request (HttpRequest): The HTTP request object

        exception (Exception): The exception that triggered the 404 error, if available.
    Returns:
        HttpResponse: The HTTP response containing the rendered oc_lettings_site 404 page

    """

    url_path = request.path
    capture_message(f"Page not found! URL: {url_path}", level="error")

    return render(request, '404.html', status=404)
