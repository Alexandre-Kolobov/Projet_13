"""
Module containing fixtures for testing purposes of lettings app.

fixtures:
    adress_instance - Returns an instance of Address model
    letting_instance - Returns an instance of Letting model

"""

import pytest
from lettings.models import Address, Letting


@pytest.fixture
def adress_instance(django_db_setup):
    """
    Fixture to create an instance of the Address model for testing purposes.

    - Creates an Address instance with predefined attributes.

    Returns:
    - An instance of the Address model for testing.

    Note:
        django_db_setup is a fixture with session scope

    """
    adress = Address.objects.create(
        number=95,
        street="Exelmans",
        city="Versailles",
        state="Fr",
        zip_code="78000",
        country_iso_code="Fr"
    )

    return adress


@pytest.fixture
def letting_instance(django_db_setup, adress_instance):
    """
    Fixture to create an instance of the Letting model for testing purposes.

    - Creates an Letting instance with predefined attributes.

    Returns:
    - An instance of the Letting model for testing.

    Note:
        django_db_setup is a fixture with session scope

    """
    letting = Letting.objects.create(
        title="House",
        address=adress_instance
    )

    return letting
