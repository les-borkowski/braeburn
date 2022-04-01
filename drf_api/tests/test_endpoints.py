import json
from urllib import response
from django.urls import reverse

def test_health(client):
    url = reverse("health")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["health"] == "OK"
    
def test_root(client):
    test_string = "sometext"
    url = f"/api/?url={test_string}"
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["url"] == test_string