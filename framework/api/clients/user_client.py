import requests

from framework.api.models.user_model import UserData, UserLogin
from constants.api_endpoints import ApiEndpoints
from framework.config import BASE_URL


class UserClient:
    def __init__(self, token: str | None = None):
        self.session = requests.Session()
        self.base_url = BASE_URL
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})


    def add_user(self, user_data: UserData) -> requests.Response:
        return self.session.post(f"{self.base_url}{ApiEndpoints.USERS}",
                             json=user_data.model_dump(by_alias=True))

    def get_user_profile(self) -> requests.Response:
        return self.session.get(f"{self.base_url}{ApiEndpoints.USERS_PROFILE}")
    
    def update_user(self, user_data: UserData) -> requests.Response:
        return self.session.put(f"{self.base_url}{ApiEndpoints.USERS_PROFILE}",
                                json=user_data.model_dump(by_alias=True))
    
    def logout_user(self) -> requests.Response:
        return self.session.post(f"{self.base_url}{ApiEndpoints.LOGOUT}")
    
    
    def login_user(self, user_data: UserLogin) -> requests.Response:
        return self.session.post(f"{self.base_url}{ApiEndpoints.LOGIN}",
                                json=user_data.model_dump(by_alias=True))
    
    def delete_user(self) -> requests.Response:
        return self.session.delete(f"{self.base_url}{ApiEndpoints.USERS_PROFILE}")
  


