"""
Module containing tests for urls of lettings app.

Functions:
    test_lettings_index_url - Tests lettings index page
    test_letting_id_urls - Tests the letting page for selected id

"""

import pytest
from django.urls import reverse, resolve


def test_lettings_index_url():
    """
    Testing URL path and view for the lettings index page.
    Checks that URL for 'lettings:index' page is correctly generated.
    And also checks that 'lettings:index' is correctly associated with URL "/lettings/"

    """

    path = reverse('lettings:index')

    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


@pytest.mark.django_db
def test_letting_id_urls():
    """
    Testing URL path and view for the one letting page by using
    a fixtures 'letting_instance' that have a session scope

    Checks that URL for 'lettings:letting' page is correctly generated.
    And also checks that 'lettings:letting' is correctly associated with URL "/lettings/1"

    """

    path = reverse('lettings:letting', kwargs={'letting_id': 1})

    assert path == "/lettings/1"
    assert resolve(path).view_name == "lettings:letting"
