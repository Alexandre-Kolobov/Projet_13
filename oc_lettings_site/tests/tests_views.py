"""
Module containing tests for views of lettings app.

Functions:
    test_lettings_index_view - Tests lettings index page view
    test_letting_id_view - Tests the letting page view for selected id

"""

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


def test_oc_lettings_site_index_view():
    """
    Test for the 'index' view.

    - Creates a client for making HTTP requests.
    - Get the URL path for the 'index' view by using reverse().
    - Sends a GET request to the URL.
    - Checks that the expected content is present in the response.
    - Verifies that the HTTP status code is 200 (OK).
    - Checks that expected template ('index.html') is used.

    """

    client = Client()

    path = reverse('index')

    response = client.get(path)
    content = response.content.decode()
    expected_content = (
        '<h1 class="page-header-ui-title mb-3 display-6">Welcome to Holiday Homes</h1>'
    )

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
