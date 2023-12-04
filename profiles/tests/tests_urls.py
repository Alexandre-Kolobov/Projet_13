"""
Module containing tests for urls of profiles app.

Functions:
    test_profiles_index_url - Tests profiles index page
    test_profile_id_urls - Tests the profile page for selected username

"""

import pytest
from django.urls import reverse, resolve


def test_profiles_index_url():
    """
    Testing URL path and view for the profiles index page.
    Checks that URL for 'profiles:index' page is correctly generated.
    And also checks that 'profiles:index' is correctly associated with URL "/profiles/"

    """

    path = reverse('profiles:index')

    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db
def test_profile_id_urls(profile_instance):
    """
    Testing URL path and view for the one profile page by using
    a fixtures 'profile_instance' that have a session scope

    Checks that URL for 'profiles:profile' page is correctly generated.
    And also checks that 'profiles:profile' is correctly associated with URL "/profiles/Alex"

    """

    path = reverse('profiles:profile', kwargs={'username': "Alex"})

    assert path == "/profiles/Alex"
    assert resolve(path).view_name == "profiles:profile"
