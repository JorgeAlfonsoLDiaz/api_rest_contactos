import csv
import json

from typing import Union
from typing import List

from fastapi import FastAPI, Request, File, UploadFile
from pydantic import BaseModel

app = FastAPI()

class Contacto(BaseModel):
    id_contactos: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    email: str
    telefono: str | None


@app.get("/", description="Endpoint raíz de la API.", summary="Endpoint raíz.")  #   // --- // Endpoint raíz \\ --- \\
def read_root():
    return {"message": "Hello World"}


@app.get("/v1/contactos", description="Endpoint para consultar datos de la API.", summary="Endpoint para consulta.", response_model=List[Contacto], status_code=200)  #   // --- // Endpoint GET contacto (todos) \\ --- \\
async def get_contacto():
    file_csv = "contactos.csv"
    response = []

    with open(file_csv, mode='r', newline='') as file:
        reader_csv = csv.DictReader(file)
        for row in reader_csv:
            response.append(row)
    return response


@app.post("/v1/contactos", description="Endpoint para enviar datos a la API.", summary="Endpoint para enviar datos.", status_code=201)  #   // --- // Endpoint POST contacto \\ --- \\
async def post_contacto(contacto: Contacto):
    file_csv = "contactos.csv"

    with open(file_csv, mode="a", newline='') as file:
        writer_csv = csv.DictWriter(file, fieldnames=["id_contactos", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"])
        writer_csv.writerow({"id_contactos": contacto.id_contactos, "nombre": contacto.nombre, "primer_apellido": contacto.primer_apellido, "segundo_apellido": contacto.segundo_apellido, "email": contacto.email, "telefono": contacto.telefono})
    
    return {"message": "Contacto registrado exitosamente"}


@app.put("/v1/contactos/{id_contactos}", description="Endpoint para actualizar datos de la API.", summary="Endpoint para actualizar.", status_code=200)  #   // --- // Endpoint PUT contacto \\ --- \\
async def put_contacto(id_contactos: int, contacto: Contacto):
    file_csv = "contactos.csv"
    response = []

    with open(file_csv, mode='r', newline='') as file:
        reader_csv = csv.DictReader(file)
        for row in reader_csv:
            if(int(row["id_contactos"]) == id_contactos):
                row.update(contacto.dict())
            response.append(row)

    with open(file_csv, mode='w', newline='') as file:
        writer_csv = csv.DictWriter(file, fieldnames=["id_contactos", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"])
        writer_csv.writeheader()
        writer_csv.writerows(response)
    
    return {"message": "Contacto actualizado exitosamente"}


@app.delete("/v1/contactos/{id_contactos}", description="Endpoint para eliminar datos de la API.", summary="Endpoint para eliminar.", status_code=200)  #   // --- // Endpoint DELETE contacto (por id_contactos) \\ --- \\
async def delete_contacto(id_contactos: int):
    file_csv = "contactos.csv"
    response = []

    with open(file_csv, mode='r', newline='') as file:
        reader_csv = csv.DictReader(file)
        for row in reader_csv:
            if(int(row["id_contactos"]) != id_contactos):
                response.append(row)    

    with open(file_csv, mode='w', newline='') as file:
        writer_csv = csv.DictWriter(file, fieldnames=["id_contactos", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"])
        writer_csv.writeheader()
        writer_csv.writerows(response)

    return {"message":"Registro eliminado correctamente."}


@app.get("/v1/contactos/", description="Endpoint para consultar datos de la API según su nombre", summary="Endpoint de búsqueda.", response_model=List[Contacto], status_code=200)  #   // --- // Endpoint GET contacto (por nombre) \\ --- \\
async def get_contacto(request: Request):
    nombre = request.query_parameters.get("nombre")

    file_csv = "contactos.csv"
    response = []

    with open(file_csv, mode='r', newline='') as file:
        reader_csv = csv.DictReader(file)
        for row in reader_csv:
            if(row["nombre"] == nombre):
                response.append(row)
    return response



@app.post("/v1/imagenes",description="Endpoint para subir una imagen a la API.", summary="Endpoint para imagen.", status_code=200)
async def post_imagen(imagen: UploadFile = File(...)):
    image_dir = "static/images"

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    file = imagen.filename

    
