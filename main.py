from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="API REST Universidad")

# Arrays en memoria requeridos
alumnos_db = []
profesores_db = []

# --- ENTIDADES ---
# Field(..., min_length=1) valida que el campo no esté vacío y los tipos aseguran el dato correcto
class Alumno(BaseModel):
    id: int
    nombres: str = Field(..., min_length=1)
    apellidos: str = Field(..., min_length=1)
    matricula: str = Field(..., min_length=1)
    promedio: float

class Profesor(BaseModel):
    id: int
    numeroEmpleado: str = Field(..., min_length=1)
    nombres: str = Field(..., min_length=1)
    apellidos: str = Field(..., min_length=1)
    horasClase: int

# --- ENDPOINTS ALUMNOS ---
@app.get("/alumnos", response_model=List[Alumno], status_code=status.HTTP_200_OK)
def get_alumnos():
    return alumnos_db

@app.get("/alumnos/{id}", response_model=Alumno, status_code=status.HTTP_200_OK)
def get_alumno(id: int):
    for a in alumnos_db:
        if a.id == id:
            return a
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

@app.post("/alumnos", response_model=Alumno, status_code=status.HTTP_201_CREATED)
def create_alumno(alumno: Alumno):
    alumnos_db.append(alumno)
    return alumno

@app.put("/alumnos/{id}", response_model=Alumno, status_code=status.HTTP_200_OK)
def update_alumno(id: int, alumno_actualizado: Alumno):
    for index, a in enumerate(alumnos_db):
        if a.id == id:
            alumnos_db[index] = alumno_actualizado
            return alumno_actualizado
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

@app.delete("/alumnos/{id}", status_code=status.HTTP_200_OK)
def delete_alumno(id: int):
    for index, a in enumerate(alumnos_db):
        if a.id == id:
            alumnos_db.pop(index)
            return {"mensaje": "Alumno eliminado"}
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

# --- ENDPOINTS PROFESORES ---
@app.get("/profesores", response_model=List[Profesor], status_code=status.HTTP_200_OK)
def get_profesores():
    return profesores_db

@app.get("/profesores/{id}", response_model=Profesor, status_code=status.HTTP_200_OK)
def get_profesor(id: int):
    for p in profesores_db:
        if p.id == id:
            return p
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

@app.post("/profesores", response_model=Profesor, status_code=status.HTTP_201_CREATED)
def create_profesor(profesor: Profesor):
    profesores_db.append(profesor)
    return profesor

@app.put("/profesores/{id}", response_model=Profesor, status_code=status.HTTP_200_OK)
def update_profesor(id: int, profesor_actualizado: Profesor):
    for index, p in enumerate(profesores_db):
        if p.id == id:
            profesores_db[index] = profesor_actualizado
            return profesor_actualizado
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

@app.delete("/profesores/{id}", status_code=status.HTTP_200_OK)
def delete_profesor(id: int):
    for index, p in enumerate(profesores_db):
        if p.id == id:
            profesores_db.pop(index)
            return {"mensaje": "Profesor eliminado"}
    raise HTTPException(status_code=404, detail="Profesor no encontrado")