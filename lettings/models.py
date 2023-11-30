"""
Module containing Django models for the lettings app.

Classes:
    Address
    Letting

"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    A class to represent an address.

    Attributes:
        number (PositiveIntegerField): The street number of the address.
        street (CharField): The name of the street (64 characters).
        city (CharField): The city where the address is located (64 characters).
        state (CharField): The state or region code (2 characters).
        zip_code (PositiveIntegerField): The ZIP code of the address.
        country_iso_code (CharField): The ISO code of the country (3 characters).

    Methods:
        __str__(): Returns a string representation of the address.

    Meta:
        verbose_name_plural (str): The plural name for the model in the Django admin.

    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Adresses"


class Letting(models.Model):
    """
    A class to represent a letting.

    Attributes:
        title (CharField): The title of letting.
        address (Address): The adress of letting.

    Methods:
        __str__(): Returns a string representation of the letting.

    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
