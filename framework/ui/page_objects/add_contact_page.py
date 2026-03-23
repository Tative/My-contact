from playwright.sync_api import Page
from framework.ui.models.contact_models_ui import ContactUI

class AddContact:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_name_field = page.get_by_test_id("firstName")
        self.last_name_field = page.get_by_test_id("lastName")
        self.birth_date_field = page.get_by_test_id("birthdate")
        self.email_field = page.get_by_test_id("email")
        self.phone_field = page.get_by_test_id("phone")
        self.address_1_field = page.get_by_test_id("street1")
        self.address_2_field = page.get_by_test_id("street2")
        self.city_field = page.get_by_test_id("city")
        self.state_province_field = page.get_by_test_id("stateProvince")
        self.postal_code_field = page.get_by_test_id("postalCode")
        self.country_field = page.get_by_test_id("country")
        self.logout_button = page.get_by_test_id("logout")
        self.submit_button = page.get_by_test_id("submit")
        self.cancel_button = page.get_by_test_id("cancel")
        self.error_text = page.get_by_test_id("error")


    def fill_form(self, contact: ContactUI):
        if contact.first_name is not None:
            self.first_name_field.fill(contact.first_name)
        if contact.last_name is not None:
            self.last_name_field.fill(contact.last_name)
        if contact.birthdate is not None:
            self.birth_date_field.fill(contact.birthdate)
        if contact.email is not None:
            self.email_field.fill(contact.email)
        if contact.phone is not None:
            self.phone_field.fill(contact.phone)
        if contact.street1 is not None:
            self.address_1_field.fill(contact.street1)
        if contact.street2 is not None:
            self.address_2_field.fill(contact.street2)
        if contact.city is not None:
            self.city_field.fill(contact.city)
        if contact.state_province is not None:
            self.state_province_field.fill(contact.state_province)
        if contact.postal_code is not None:
            self.postal_code_field.fill(contact.postal_code)
        if contact.country is not None:
            self.country_field.fill(contact.country)

    
    def logout(self):
        self.logout_button.click()

    def submit(self):
        self.submit_button.click()

    def cancel(self):
        self.cancel_button.click()
