from pydantic import BaseModel
from typing import Optional

class RoofCreate(BaseModel):
    longitud: float
    latitud: float
    image: Optional[str] = None  # Esta es opcional
    user_id: Optional[int] = None  # Esta es opcional
    price: float

class Roof(RoofCreate):
    id: int

    class Config:
        orm_mode = True  # Para convertir el modelo de SQLAlchemy en dict
