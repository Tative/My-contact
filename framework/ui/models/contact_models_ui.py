from pydantic import BaseModel


class ContactUI(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    birthdate: str | None = None
    email: str | None = None
    phone: str | None = None
    street1: str | None = None
    street2: str | None = None
    city: str | None = None
    state_province: str | None = None
    postal_code: str | None = None
    country: str | None = None