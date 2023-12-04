"""
Module containing tests for views of lettings app.

Functions:
    test_lettings_index_view - Tests lettings index page view
    test_letting_id_view - Tests the letting page view for selected id

"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_lettings_index_view(letting_instance):
    """
    Test for the 'lettings:index' view.

    - Creates a client for making HTTP requests.
    - Uses a fixture 'letting_instance' to create an instance
      of the letting model for testing purposes.
    - Get the URL path for the 'lettings:index' view by using reverse().
    - Sends a GET request to the URL.
    - Checks that the expected content is present in the response.
    - Verifies that the HTTP status code is 200 (OK).
    - Checks that expected template ('lettings/index.html') is used.

    """

    client = Client()

    letting = letting_instance

    path = reverse('lettings:index')

    response = client.get(path)
    content = response.content.decode()
    expected_content = f'<a href="/lettings/1">{letting.title}</a>'

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_id_view(letting_instance, adress_instance):
    """
    Test for the 'lettings:letting' view.

    - Creates a client for making HTTP requests.
    - Uses a fixtures 'letting_instance' and 'adress_instance'
      to create instances of the letting and adress models for testing purposes.
    - Get the URL path for the 'lettings:letting'
      view by using reverse() with kwargs={'letting_id':1}.
    - Sends a GET request to the URL.
    - Checks that the expected content is present in the response.
    - Verifies that the HTTP status code is 200 (OK).
    - Checks that expected template ('lettings/letting.html') is used.

    """

    client = Client()
    adress = adress_instance
    letting = letting_instance

    path = reverse('lettings:letting', kwargs={'letting_id': 1})

    response = client.get(path)
    content = response.content.decode()
    expected_content_header = (
        '<h1 class="page-header-ui-title mb-3 display-6">'
        f'{letting.title}'
        '</h1>'
        )

    expected_content_street = f'<p>{adress.number} {adress.street}</p>'
    expected_content_city = f'<p>{adress.city}, {adress.state} {adress.zip_code}</p>'
    expected_content_country = f'<p>{adress.country_iso_code}</p>'

    assert expected_content_header in content
    assert expected_content_street in content
    assert expected_content_city in content
    assert expected_content_country in content

    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
