"""
Module containing tests for views of profiles app.

Functions:
    test_profiles_index_view - Tests profiles index page view
    test_profile_id_view - Tests the profile page view for selected username

"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profiles_index_view(profile_instance):
    """
    Test for the 'profiles:index' view.

    - Creates a client for making HTTP requests.
    - Uses a fixture 'profile_instance' to create an instance
      of the profile model for testing purposes.
    - Get the URL path for the 'profiles:index' view by using reverse().
    - Sends a GET request to the URL.
    - Checks that the expected content is present in the response.
    - Verifies that the HTTP status code is 200 (OK).
    - Checks that expected template ('profiles/index.html') is used.

    """

    client = Client()

    profile = profile_instance

    path = reverse('profiles:index')

    response = client.get(path)
    content = response.content.decode()
    expected_content = f'<a href="/profiles/Alex">{profile.user.username}</a>'

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_id_view(profile_instance):
    """
    Test for the 'profiles:profile' view.

    - Creates a client for making HTTP requests.
    - Uses a fixtures 'profile_instance'
      to create instances of the profiles model for testing purposes.
    - Get the URL path for the 'profiles:profile'
      view by using reverse() with kwargs={'username':'Alex'}.
    - Sends a GET request to the URL.
    - Checks that the expected content is present in the response.
    - Verifies that the HTTP status code is 200 (OK).
    - Checks that expected template ('profiles/profile.html') is used.

    """

    client = Client()
    profile = profile_instance

    path = reverse('profiles:profile', kwargs={'username': profile.user.username})

    response = client.get(path)
    content = response.content.decode()
    expected_content_header = (
        '<h1 class="page-header-ui-title mb-3 display-6">'
        f'{profile.user.username}'
        '</h1>'
        )

    assert expected_content_header in content

    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
