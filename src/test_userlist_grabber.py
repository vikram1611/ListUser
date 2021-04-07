import requests
import pytest

def test_userlist_status_code():
    response = requests.get('https://reqres.in/api/users?page=2', timeout=10)
    assert response.status_code == 200

def test_userlist_not_empty():
    response = requests.get('https://reqres.in/api/users?page=2', timeout=10)
    assert len(response.json()) != 0 