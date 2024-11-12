from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import DECIMAL
from app.database import Base

class Roof(Base):
    __tablename__ = 'roof'

    id = Column(Integer, primary_key=True, index=True)
    longitud = Column(DECIMAL(10, 6), nullable=False)
    latitud = Column(DECIMAL(10, 6), nullable=False)
    image = Column(String(255), nullable=True)  # Opcional
    user_id = Column(Integer, nullable=True)    # Opcional
    price = Column(DECIMAL(10, 2), nullable=False)
