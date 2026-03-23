from pydantic import BaseModel, Field, ConfigDict

# Базовые поля юзера (используется в регистрации и обновлении)
class UserBase(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    email: str

#ОТВЕТ: Юзер с ID
class UserResponse(UserBase):
    id: str = Field(alias='_id')

#ОТВЕТ: на логин и регистрацию (юзер + токен)
class UserLoginResponse(BaseModel):
    user: UserResponse
    token: str

#ЗАПРОС: на логин
class UserLogin(BaseModel):
    email: str
    password: str

#ЗАПРОС на регистрацию и обновление юзера
class UserData(UserBase):
    password: str

