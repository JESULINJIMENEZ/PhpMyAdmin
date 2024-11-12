from sqlalchemy.orm import Session
from app import models, schemas

def create_roof(db: Session, roof: schemas.RoofCreate):
    db_roof = models.Roof(
        longitud=roof.longitud,
        latitud=roof.latitud,
        image=roof.image,
        user_id=roof.user_id,
        price=roof.price
    )
    db.add(db_roof)
    db.commit()
    db.refresh(db_roof)
    return db_roof

def get_roof(db: Session, roof_id: int):
    return db.query(models.Roof).filter(models.Roof.id == roof_id).first()
