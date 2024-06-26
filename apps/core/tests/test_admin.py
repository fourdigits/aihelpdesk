from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.usefixtures("home_page")
def test_django_admin_login_shows_release_version_from_setting(django_app, settings):
    response = django_app.get(reverse("admin:login"))
    assert response.status_code == HTTPStatus.OK
    assert f"ai-helpdesk versie {settings.RELEASE_VERSION} in response"
