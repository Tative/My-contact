from framework.api.clients.user_client import UserClient
from framework.api.models.user_model import UserResponse, UserLoginResponse,UserData, UserLogin



class UserHelpers:
    def __init__(self, client: UserClient):
        self.client = client
        
    def register_new_user(self, user_data: UserData) -> UserLoginResponse:
        response = self.client.add_user(user_data)
        response.raise_for_status()
        return UserLoginResponse(**response.json())
    
    def get_user_profile_data(self) -> UserResponse:
        response = self.client.get_user_profile()
        response.raise_for_status()
        return UserResponse(**response.json())
    
    def change_profile_data(self, user_data: UserData) -> UserResponse:
        response = self.client.update_user(user_data)
        response.raise_for_status()
        return UserResponse(**response.json())
    
    def logout_user(self) -> None:
        response = self.client.logout_user()
        response.raise_for_status()
        
    def authorize_user(self, user_data: UserLogin) -> UserLoginResponse:
        response = self.client.login_user(user_data)
        response.raise_for_status()
        return UserLoginResponse(**response.json())
    
    
    def delete_user(self) -> None:
        response = self.client.delete_user()
        response.raise_for_status()