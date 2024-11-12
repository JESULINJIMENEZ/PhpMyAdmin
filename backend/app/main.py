# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

# Crear todas las tablas en la base de datos (si no existen)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/roof/", response_model=schemas.Roof)
def create_roof(roof: schemas.RoofCreate, db: Session = Depends(get_db)):
    try:
        db_roof = crud.create_roof(db=db, roof=roof)
        return db_roof
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el techo: {str(e)}")

@app.get("/roof/{roof_id}", response_model=schemas.Roof)
def read_roof(roof_id: int, db: Session = Depends(get_db)):
    try:
        db_roof = crud.get_roof(db=db, roof_id=roof_id)
        if db_roof is None:
            raise HTTPException(status_code=404, detail="Techo no encontrado")
        return db_roof
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el techo: {str(e)}")
