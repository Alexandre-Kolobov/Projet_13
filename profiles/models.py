"""
Module containing Django models for the profiles app.

Classes:
    Profile

"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class to represent a profile.

    Attributes:
        user (User): The user attached to this profile.

        favorite_city (CharField): The name of the user's favorite city (64 characters).

    Methods:
        __str__(): Returns a string representation of the profile.

    Meta:
        verbose_name_plural (str): The plural name for the model in the Django admin.

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
