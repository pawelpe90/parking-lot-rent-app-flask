from pydantic import BaseModel, Field
from typing_extensions import Annotated


class User(BaseModel):
    name: Annotated[str, Field(min_length=2)]
    surname: Annotated[str, Field(min_length=2)]
    username: Annotated[str, Field(min_length=2)]
    email: Annotated[str, Field(pattern=r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$')]
    phone: Annotated[str, Field(pattern=r'^(?:\+48)?[1-9][0-9]{8}$', description='Numer powinien składać się dziewięciu cyfr z opcjonalnym prefiksem.')]
    password: Annotated[str, Field(min_length=5)]
    parking_lot_number: Annotated[str, Field(pattern='^[1-9][0-9]{2}$')]
