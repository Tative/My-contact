import requests

from framework.api.models.user_model import UserData, UserLoginResponse
from constants.api_endpoints import ApiEndpoints
from framework.config import BASE_URL


class UserClient:
    def __init__(self):
        self.base_url = BASE_URL

    def create_user(self, user_data: UserData) -> UserLoginResponse:
        response = requests.post(
            f"{BASE_URL}{ApiEndpoints.USERS}",
            json=user_data.model_dump(by_alias=True)
        )
        response.raise_for_status()
        return UserLoginResponse(**response.json())


    def delete_user(self, token: str) -> None:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(f"{BASE_URL}{ApiEndpoints.USERS_PROFILE}", headers=headers)
        response.raise_for_status()


