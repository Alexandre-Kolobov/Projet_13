"""
Module containing tests for urls of oc_lettings_site app.

Functions:
    test_oc_lettings_site_index_url - Tests oc_lettings_site index page
    test_oc_lettings_site_admin_url - Tests the admin page

"""


from django.urls import reverse, resolve
from django.test import Client


def test_oc_lettings_site_index_url():
    """
    Testing URL path and view for the oc_lettings_site index page.
    Checks that URL for 'index' page is correctly generated.
    And also checks that 'index' is correctly associated with URL "/"

    """

    path = reverse('index')

    assert path == "/"
    assert resolve(path).view_name == "index"


def test_oc_lettings_site_admin_url():
    """
    Testing URL path and view for the admin page.
    Checks that URL for admin page is correctly generated.
    Checks the status code and content.

    """

    client = Client()

    admin_url = reverse('admin:index')
    response = client.get(admin_url, follow=True)
    content = response.content.decode()
    expected_content = 'Django administration'

    assert response.status_code == 200
    assert expected_content in content
