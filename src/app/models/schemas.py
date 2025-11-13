from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(..., example="Igorzon")
    email: str = Field(..., example="igor@example.com")

class OrderCreate(BaseModel):
    user_id: str = Field(..., example="64f2a8c78f9b1d23e4c9e7a3")
    amount: float = Field(..., example=150.75)
