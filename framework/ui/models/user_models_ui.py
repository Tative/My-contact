from pydantic import BaseModel


class UserLoginUI(BaseModel):
    email: str | None = None
    password: str | None = None


class UserRegistrationUI(UserLoginUI):
    first_name: str | None = None
    last_name: str | None = None