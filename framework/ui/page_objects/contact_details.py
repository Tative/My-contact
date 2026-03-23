from playwright.sync_api import Page


class ContactDetails:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.edit_button = page.get_by_test_id("edit-contact")
        self.delete_button = page.get_by_test_id("delete")
        self.return_to_contact_button = page.get_by_test_id("return")
        self.logout_button = page.get_by_test_id("logout")


    def delete_contact_accept(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.delete_button.click()


    def return_to_contact(self):
        self.return_to_contact_button.click()

    def edit_contact(self):   
        self.edit_button.click()
