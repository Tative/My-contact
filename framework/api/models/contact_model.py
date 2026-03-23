from pydantic import BaseModel, Field, ConfigDict


class Contact(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_name: str | None = Field(default=None, alias='firstName')
    last_name: str | None = Field(default=None, alias='lastName')
    birthdate: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    street1: str | None = Field(default=None)
    street2: str | None = Field(default=None)
    city: str | None = Field(default=None)
    state_province: str | None = Field(default=None, alias='stateProvince')
    postal_code: str | None = Field(default=None, alias='postalCode')
    country: str | None = Field(default=None)

class ContactResponse(Contact):
    id: str = Field(alias="_id")
    owner: str
