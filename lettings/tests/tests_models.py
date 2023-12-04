"""
Module containing tests for models of lettings app.

Functions:
    test_adress_model - Tests Address model
    test_letting_model - Tests Letting model

"""

import pytest


@pytest.mark.django_db
def test_adress_model(adress_instance):
    """
    Test for the string representation of the Address model.

    - Uses a fixture 'adress_instance' to create an instance of the Address model for testing.
    - Defines the expected string representation based on the address attributes.
    - Asserts that the actual string representation matches the expected value.

    """

    adress = adress_instance

    expected_value = f'{adress.number} {adress.street}'
    assert str(adress) == expected_value


@pytest.mark.django_db
def test_letting_model(letting_instance):
    """
    Test for the string representation of the Letting model.

    - Uses a fixture 'letting_instance' to create an instance of the Letting model for testing.
    - Defines the expected string representation based on the letting attributes.
    - Asserts that the actual string representation matches the expected value.

    """

    letting = letting_instance

    expected_value = f'{letting.title}'
    assert str(letting) == expected_value
