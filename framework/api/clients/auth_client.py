import requests
from framework.config import BASE_URL
from framework.api.models.user_model import UserResponse, UserLogin, UserLoginResponse
from constants.api_endpoints import ApiEndpoints


class AuthClient:
    def __init__(self):
        self.base_url = BASE_URL

    def login(self, email, password) -> UserLoginResponse:
        payload = UserLogin(email=email, password=password)
        response = requests.post(f"{BASE_URL}{ApiEndpoints.LOGIN}", json=payload.model_dump())
        response.raise_for_status()
        return UserLoginResponse(**response.json())
    
