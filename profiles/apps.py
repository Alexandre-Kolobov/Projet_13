"""
Module containing Django profiles app.

Classes:
    ProfilesConfig

"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    AppConfig for the profiles app.

    Attributes:
        name (str): The name of the Django app 'profiles'.

    """

    name = 'profiles'
