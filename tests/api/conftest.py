import pytest
import requests
from typing import Generator
from faker import Faker


from framework.api.clients.user_client import UserClient
from framework.api.clients.contacts_client import ContactClient
from framework.api.models.user_model import UserData, UserLogin, UserLoginResponse, UserResponse
from framework.api.models.contact_model import Contact, ContactResponse


fake = Faker()

@pytest.fixture
def user_create() -> Generator[requests.Response, None, None]:
    user_data = UserData(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password="password"      
    )
    user = UserClient()
    user_response = user.add_user(user_data)
    
    yield user_response
    user_schema = UserLoginResponse(**user_response.json())
    user.delete_user(user_schema.token)
    
    
@pytest.fixture
def contact_create(user_create: requests.Response) -> Generator[requests.Response, None, None]:
    contact_data = Contact(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birthdate=fake.date(),
        email=fake.email(),
        phone=fake.numerify(text='##########'),
        street1=fake.street_address(),
        street2=fake.street_address(),
        city=fake.city(),
        state_province=fake.state(),
        postal_code=fake.postalcode(),
        country=fake.country()
    )
    user_schema = UserLoginResponse(**user_create.json())
    contact = ContactClient(user_schema.token)
    created_contact = contact.add_contact(contact_data)
    yield created_contact
    contact_schema = ContactResponse(**created_contact.json())
    contact.delete_contact(contact_schema.id)
    
    #todo: разбить фикстуру contact_create. Отельно создание данные, отдельно создание контакта
    #понять нужен ли токен в создании юзера
    