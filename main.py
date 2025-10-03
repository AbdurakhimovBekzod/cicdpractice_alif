import requests
import pytest

base_url = "https://gw.alifshop.uz"
active_items_url = f"{base_url}/web/client/events/active"
get_item = f"{base_url}/web/client/moderated-offers"


def url_generator(slug):
    return f"{get_item}/{slug}"


@pytest.fixture
def item_slug():
    response = requests.get(url=active_items_url)
    assert response.status_code == 200
    response = response.json()
    return response[0]['offers'][0]['slug']


def test_active_items(item_slug):
    assert item_slug is not None
    print(f"Slug: {item_slug}")


def test_get_item(item_slug):
    url = url_generator(item_slug)
    response = requests.get(url=url)
    assert response.status_code == 200
    print(response.json())
