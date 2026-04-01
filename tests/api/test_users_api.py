import pytest
import requests


from framework.api.clients.contacts_client import ContactClient
from framework.api.models.user_model import UserData, UserLogin, UserLoginResponse, UserResponse
from framework.api.models.contact_model import Contact, ContactResponse


def test_user_data(user_create: requests.Response) -> None:
    assert user_create.status_code == 201, f"\nExpected: 201\nActual: {user_create.status_code}"
    
def test_contact_create(contact_create: requests.Response) -> None:
    assert contact_create.status_code == 201
    

    