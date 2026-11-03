"""
Module: controllers.py
Description: RESTful FastAPI Application endpoints for Lab 4 migration.
Author: Solomon Azowenu
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field
import models

app = FastAPI(
    title="SEN 401 Re-Engineered API",
    version="2.0.0",
    description="Re-engineered application backend with SQLite and FastAPI"
)

models.init_db()

class StudentSchema(BaseModel):
    name: str = Field(..., min_length=1)
    score: float = Field(..., ge=0, le=100)

@app.get("/")
def read_root():
    return {"status": "Online", "message": "SEN 401 Re-Engineered API Service"}

@app.get("/students")
def read_students():
    return {"students": models.get_all_students()}

@app.post("/students", status_code=201)
def create_student(payload: StudentSchema):
    student_id = models.add_student_db(payload.name, payload.score)
    return {"message": "Student created successfully", "id": student_id, "data": payload}