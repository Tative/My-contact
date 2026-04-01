import requests

from framework.config import BASE_URL
from constants.api_endpoints import ApiEndpoints
from framework.api.models.contact_model import Contact, ContactResponse

    
class ContactClient:
    def __init__(self, token: str):
        self.session = requests.Session()
        self.base_url = BASE_URL
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def add_contact(self, contact_data: Contact) -> requests.Response:
        url = f"{self.base_url}{ApiEndpoints.CONTACTS}"
        return self.session.post(url, json=contact_data.model_dump(by_alias=True))
    
    def get_contact(self, contact_id: str) -> requests.Response:
        url = f"{self.base_url}{ApiEndpoints.CONTACTS}/{contact_id}"
        return self.session.get(url)

    def get_contact_list(self) -> requests.Response:
        url = f"{self.base_url}{ApiEndpoints.CONTACTS}"
        return self.session.get(url)
    
    def patch_contact(self, contact_data: ContactResponse) -> requests.Response:
        url = f"{self.base_url}{ApiEndpoints.CONTACTS}/{contact_data.id}"
        return self.session.patch(url, json=contact_data.model_dump(by_alias=True))
    
    def put_contact(self, contact_data: ContactResponse) -> requests.Response:
        url = f"{self.base_url}{ApiEndpoints.CONTACTS}/{contact_data.id}"
        return self.session.put(url, json=contact_data.model_dump(by_alias=True))

    def delete_contact(self, contact_id: str) -> requests.Response:
        url = (f"{BASE_URL}{ApiEndpoints.CONTACTS}/{contact_id}")
        return self.session.delete(url)