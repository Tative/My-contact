import pytest
from typing import Generator


from playwright.sync_api import Playwright
from playwright.sync_api import Page
from faker import Faker


from framework.api.models.user_model import UserData, UserLoginResponse
from framework.api.clients.user_client import UserClient
from framework.ui.models.contact_models_ui import ContactUI
from constants.ui_endpoints import UiEndpoints
from framework.config import BASE_URL
from framework.logic.contact_helpers import ContactHelpers
from framework.logic.user_helpers import UserHelpers
from framework.api.clients.contacts_client import ContactClient


fake = Faker()

@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("id")

@pytest.fixture
def new_user() -> Generator[UserLoginResponse, None, None]:
    client = UserHelpers(UserClient())
    password = fake.password(length=10)
    user_data = UserData(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=password
    )
    created_user = client.register_new_user(user_data)

    yield created_user

    clients = UserHelpers(UserClient(created_user.token))
    clients.delete_user()


@pytest.fixture
def contact_helpers(new_user: UserLoginResponse) -> ContactHelpers:
    return ContactHelpers(ContactClient(new_user.token))

    
@pytest.fixture
def logged_in_page(page: Page, new_user: UserLoginResponse) -> Generator[Page, None, None]:
    page.context.add_cookies([{"name": "token", "value": new_user.token, "url": BASE_URL}])

    yield page


@pytest.fixture
def fill_contact_data() -> ContactUI:
    return ContactUI(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birthdate="2000-12-12",
        email=fake.email(),
        phone=fake.numerify(text='##########'),
        street1=fake.street_name(),
        street2=fake.street_name(),
        city=fake.city(),
        state_province=fake.state(),
        postal_code=fake.postalcode(),
        country=fake.country()
    )



    
