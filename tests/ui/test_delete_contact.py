import pytest

from playwright.sync_api import Page, expect

from framework.ui.page_objects.add_contact_page import AddContact
from framework.ui.page_objects.contact_details import ContactDetails
from framework.ui.models.contact_models_ui import ContactUI
from framework.api.models.user_model import UserLoginResponse
from constants.ui_endpoints import UiEndpoints
from constants.ui_texts import ErrorInvalid
from framework.api.clients.contacts_client import ContactClient
from framework.api.clients.contacts_client import Contact

from framework.config import BASE_URL


VALID_BASELINE_CONTACT = ContactUI(
    first_name="StaticName",
    last_name="StaticLastName",
    birthdate="2000-01-01",
    email="static@test.com",
    phone="8005003030",
    street1="Street1",
    street2="=Street2",
    city="City",
    state_province="State",
    postal_code="12312",
    country="Country"
)


@pytest.fixture
def api_contact_create(new_user: UserLoginResponse):
    client = ContactClient()
    api_contact_data = Contact(**VALID_BASELINE_CONTACT.model_dump())
    response = client.create_contact(new_user.token, api_contact_data)

    yield response 

