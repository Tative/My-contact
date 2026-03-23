import requests

from framework.config import BASE_URL
from constants.api_endpoints import ApiEndpoints
from framework.api.models.contact_model import Contact, ContactResponse


class ContactClient:
    def __init__(self):
        self.base_url = BASE_URL

    def create_contact(self, token: str, contact_data: Contact) -> ContactResponse:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(f"{BASE_URL}{ApiEndpoints.CONTACTS}",
                                 json=contact_data.model_dump(by_alias=True), headers=headers)
        response.raise_for_status()
        return ContactResponse(**response.json())
    
    def get_contact(self, token: str, contact_id: str) -> ContactResponse:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}{ApiEndpoints.CONTACTS}/{contact_id}", headers=headers)
        response.raise_for_status()
        return ContactResponse(**response.json())
    
    def get_contact_list(self, token: str) -> list[ContactResponse]:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}{ApiEndpoints.CONTACTS}", headers=headers)
        response.raise_for_status()
        return [ContactResponse(**item) for item in response.json()]