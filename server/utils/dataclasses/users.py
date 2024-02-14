from pydantic import BaseModel, Field


class UserSignupSchema(BaseModel):
    user_name: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_name": "username123",
                "password": "strong_secret_password",
            }
        }


class UserLoginSchema(BaseModel):
    user_name: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_name": "username123",
                "password": "strong_secret_password",
            }
        }
