import pytest

from playwright.sync_api import Page, expect

from framework.ui.page_objects.add_contact_page import AddContact
from framework.ui.models.contact_models_ui import ContactUI
from framework.api.clients.contacts_client import ContactClient
from framework.api.models.user_model import UserLoginResponse
from constants.ui_endpoints import UiEndpoints
from constants.ui_texts import ErrorInvalid
from framework.logic.contact_helpers import ContactHelpers
from framework.logic.user_helpers import UserHelpers


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
def add_contact_page(logged_in_page: Page) -> AddContact:
    logged_in_page.goto(f"{BASE_URL}{UiEndpoints.CONTACT_ADD}")
    return AddContact(logged_in_page)


def test_user_can_create_contact(contact_helpers: ContactHelpers,
                                 add_contact_page: AddContact, fill_contact_data: ContactUI):
    add_contact_page.fill_form(fill_contact_data)
    add_contact_page.submit()
    expect(add_contact_page.page).to_have_url(f"{BASE_URL}{UiEndpoints.CONTACT_LIST}")

    contacts_from_api = contact_helpers.get_contact_list()
    
    assert len(contacts_from_api) == 1, "Контакт не сохранился в БД!"
    
    api_data = contacts_from_api[0].model_dump(exclude={'id', 'owner'}) # Выкидываем системные поля API
    expected_data = fill_contact_data.model_dump()

    assert api_data == expected_data, f"Данные в БД не совпадают! Ожидали {expected_data}, получили {api_data}"


@pytest.mark.parametrize("filled_info, expected_error", [
    #Обязательны к заполнению
    ({"first_name": ""}, ErrorInvalid.FIRST_NAME_REQ),
    ({"last_name": ""}, ErrorInvalid.LAST_NAME_REQ),
    #Неверный формат
    ({"birthdate": "123-123-123"}, ErrorInvalid.BIRTHDATE),
    ({"email": "asdmail"}, ErrorInvalid.EMAIL),
    ({"phone": "999"}, ErrorInvalid.PHONE),
    ({"postal_code": "1"}, ErrorInvalid.POSTAL_CODE),
    #Максимальная длина
    ({"first_name": "abc" * 20}, ErrorInvalid.FIRST_NAME_LONG),
    ({"last_name": "abc" * 20}, ErrorInvalid.LAST_NAME_LONG),
    ({"phone": "800" * 20}, ErrorInvalid.PHONE_LONG),
    ({"street1": "abc" * 20}, ErrorInvalid.STREET1_LONG),
    ({"street2": "abc" * 20}, ErrorInvalid.STREET2_LONG),
    ({"city": "abc" * 20}, ErrorInvalid.CITY_LONG),
    ({"state_province": "abc" * 20}, ErrorInvalid.STATE_PROVINCE_LONG),
    ({"postal_code": "123" * 20}, ErrorInvalid.POSTAL_CODE_LONG),
    ({"country": "abc" * 20}, ErrorInvalid.COUNTRY_LONG),
])
def test_add_contact_validation_errors(contact_helpers: ContactHelpers,
                                       add_contact_page: AddContact,
                                       filled_info: dict, expected_error: str):
    test_data = VALID_BASELINE_CONTACT.model_copy(update=filled_info)
    add_contact_page.fill_form(test_data)
    add_contact_page.submit()
    expect(add_contact_page.error_text).to_contain_text(expected_error)

    expect(add_contact_page.page).to_have_url(f"{BASE_URL}{UiEndpoints.CONTACT_ADD}")
    
    contacts_from_api = contact_helpers.get_contact_list()
    assert len(contacts_from_api) == 0, "Контакт сохранился в БД!"


def test_cancel_button(add_contact_page: AddContact):
    add_contact_page.cancel()
    expect(add_contact_page.page).to_have_url(f"{BASE_URL}{UiEndpoints.CONTACT_LIST}")

    