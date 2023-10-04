import csv
import json

from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Contacto(BaseModel):
    id_contactos: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    email: str
    telefono: str | None

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/v1/contactos")
async def get_contactos():
    file_csv = "contactos.csv"
    response = []

    with open(file_csv, mode='r', newline='') as file:
        reader_csv = csv.DictReader(file)
        for row in reader_csv:
            response.append(row)
    return response

@app.post("/v1/contactos")
async def post_contacto(contacto: Contacto):
    file_csv = "contactos.csv"

    with open(file_csv, mode="a", newline='') as file:
        writer_csv = csv.DictWriter(file, fieldnames=["id_contactos", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"])
        writer_csv.writerow({"id_contactos": contacto.id_contactos, "nombre": contacto.nombre, "primer_apellido": contacto.primer_apellido, "segundo_apellido": contacto.segundo_apellido, "email": contacto.email, "telefono": contacto.telefono})
    
    return {"message": "Contacto registrado exitosamente"}

