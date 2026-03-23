from playwright.sync_api import Page


class ContactList:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.logout_button = page.get_by_test_id("logout")
        self.add_contact_button = page.get_by_test_id("add-contact")
        self.table = page.get_by_test_id("myTable")

    def logout(self) -> None:
        self.logout_button.click()

    def add_contact(self) -> None:
        self.add_contact_button.click()

    