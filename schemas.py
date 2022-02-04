from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    full_name: str
    username: str
    password: str


class AddBookRequest(BaseModel):
    title: str
    author: str
    description: str
