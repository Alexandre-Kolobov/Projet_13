"""
Module containing Django views for the oc_lettings_site app.

Functions:
    index - Render the oc_lettings_site index page

"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    Render the oc_lettings_site index page

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The HTTP response containing the rendered oc_lettings_site index page

    """

    return render(request, 'index.html')
