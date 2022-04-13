import json
from django.urls import reverse


def test_health(client):
    url = reverse("health")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["health"] == "OK"


def test_api_url_invalid(client):
    test_string = "sometext"
    url = f"/api/?url={test_string}"
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert type(content['message']) == str


def test_api_url_valid(client):
    test_string = "https://bbc.co.uk"
    url = f"/api/?url={test_string}"
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert type(content['data']) == dict
