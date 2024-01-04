"""
Module containing Django views for the profile app.

Functions:
    index - Render the profiles index page

    profile - Render the profile page for selected username

"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Profile


def index(request: HttpRequest) -> HttpResponse:
    """
    Render the profiles index page

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The HTTP response containing the rendered profiles index page

    """

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    Render the profile page for selected username

    Parameters:
        request (HttpRequest): The HTTP request object

        username (str): The username of selected profile

    Returns:
        HttpResponse: The HTTP response containing the rendered profile object's page

    """

    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
