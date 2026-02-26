from pydantic import BaseModel


class CreateProductSchema(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    image_url: str

