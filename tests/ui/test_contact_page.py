import pytest
from playwright.sync_api import Page, expect
from framework.ui.page_objects.contact_list_page import ContactList
from framework.config import BASE_URL
from constants.ui_endpoints import UiEndpoints


@pytest.fixture
def contact_list(logged_in_page: Page) -> ContactList:
    return ContactList(logged_in_page)


def test_empty_contact_list_for_new_user(contact_list: ContactList) -> None:
    expect(contact_list.table).not_to_be_visible()

    
def test_add_contact_button_is_visible(contact_list: ContactList) -> None:
    expect(contact_list.add_contact_button).to_be_visible()


def test_add_contact_button_navigate(contact_list: ContactList) -> None:
    contact_list.add_contact()
    expect(contact_list.page).to_have_url(f"{BASE_URL}{UiEndpoints.CONTACT_ADD}")


def test_add_contact_button_text(contact_list: ContactList) -> None:
    expect(contact_list.add_contact_button).to_have_text("Add a New Contact")


def test_logout_button_is_visible(contact_list: ContactList) -> None:
    expect(contact_list.logout_button).to_be_visible()


# def test_logout_button_navigate(contact_list: ContactList) -> None:
#     contact_list.logout()
#     expect(contact_list.page).to_have_url(f"{BASE_URL}/")


def test_logout_button_text(contact_list: ContactList) -> None:
    expect(contact_list.logout_button).to_have_text("Logout")
