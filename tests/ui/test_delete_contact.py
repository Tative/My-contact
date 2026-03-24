import pytest

from playwright.sync_api import Page, expect

from framework.ui.page_objects.contact_details import ContactDetails
from framework.ui.page_objects.contact_list_page import ContactList
from framework.ui.models.contact_models_ui import ContactUI
from constants.ui_endpoints import UiEndpoints
from framework.api.clients.contacts_client import Contact, ContactClient
from framework.api.models.user_model import UserLoginResponse
from framework.api.models.contact_model import ContactResponse
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
def api_contact(new_user: UserLoginResponse) -> ContactResponse: # type: ignore
    client = ContactClient() 
    api_data = Contact(**VALID_BASELINE_CONTACT.model_dump())
    my_contact = client.create_contact(new_user.token, api_data) 
    
    yield my_contact
    
    try:
        client.delete_contact(new_user.token, my_contact.id)
    except:
        pass
    
@pytest.fixture
def user_on_contact_details(logged_in_page: Page, api_contact: ContactResponse) -> ContactDetails:
    logged_in_page.goto(f"{BASE_URL}{UiEndpoints.CONTACT_LIST}")
    contact_list = ContactList(logged_in_page)
    contact_list.contact_details_navigate()
    return ContactDetails(logged_in_page)

def test_user_can_delete(user_on_contact_details: ContactDetails,new_user: UserLoginResponse) -> None:    
    user_on_contact_details.delete_contact_accept()

    contact_list_page = ContactList(user_on_contact_details.page)
    expect(contact_list_page.table).not_to_be_visible()

    contact_client = ContactClient()
    contacts_from_api = contact_client.get_contact_list(new_user.token)
    assert len(contacts_from_api) == 0
       
    