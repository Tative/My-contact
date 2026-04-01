from framework.api.clients.contacts_client import ContactClient
from framework.api.models.contact_model import ContactResponse, Contact

class ContactHelpers:
    def __init__(self, client: ContactClient):
        self.client = client
        
    def create_new_contact(self, contact_data: Contact) -> ContactResponse:
        response = self.client.add_contact(contact_data)
        response.raise_for_status()
        return ContactResponse(**response.json())
    
    def get_contact_info(self, contact_id: str) -> ContactResponse:
        response = self.client.get_contact(contact_id)
        response.raise_for_status()
        return ContactResponse(**response.json())
    
    def get_contact_list(self) -> list[ContactResponse]:
        response = self.client.get_contact_list()
        response.raise_for_status()
        return [ContactResponse(**item) for item in response.json()]
    
    def patch_update_contact(self, contact_data: Contact) -> ContactResponse:
        response = self.client.patch_contact(contact_data)
        response.raise_for_status()
        return ContactResponse(**response.json())
    
    def put_update_contact(self, contact_data: Contact) -> ContactResponse:
        response = self.client.put_contact(contact_data)
        response.raise_for_status()
        return ContactResponse(**response.json())
    
    def delete_contact(self, contact_id: str) -> None:
        response = self.client.delete_contact(contact_id)
        response.raise_for_status()