"""
Module containing fixtures for testing purposes of profiles app.

fixtures:
    prfoile_instance - Returns an instance of Profile model

"""

import pytest
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.fixture
def profile_instance(django_db_setup):
    """
    Fixture to create an instance of the Profile model for testing purposes.

    - Creates an Profile instance with predefined attributes.

    Returns:
    - An instance of the Profile model for testing.

    Note:
        django_db_setup is a fixture with session scope

    """
    profile = Profile.objects.create(
        user=User.objects.create(username="Alex", password="test"),
        favorite_city="Versailles"
    )

    return profile
