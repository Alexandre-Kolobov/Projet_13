"""
Module containing tests for models of profiles app.

Functions:
    test_profile_model - Tests Profile model

"""

import pytest


@pytest.mark.django_db
def test_profile_model(profile_instance):
    """
    Test for the string representation of the Profile model.

    - Uses a fixture 'profile_instance' to create an instance of the Profile model for testing.
    - Defines the expected string representation based on the Profile attributes.
    - Asserts that the actual string representation matches the expected value.

    """

    profile = profile_instance

    expected_value = f'{profile.user.username}'
    assert str(profile) == expected_value
