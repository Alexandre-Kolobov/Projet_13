"""
Module containing Django views for the lettings app.

Functions:
    index - Render the lettings index page.

    letting - Render the letting page for selected id.

"""


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Letting


def index(request: HttpRequest) -> HttpResponse:
    """
    Render the lettings index page

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The HTTP response containing the rendered lettings index page

    """

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    Render the letting page for selected id

    Parameters:
        request (HttpRequest): The HTTP request object

        letting_id (int): The id of letting object

    Returns:
        HttpResponse: The HTTP response containing the rendered letting object's page

    """

    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
