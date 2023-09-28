from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"mesage": "Hello World"}

@app.get("/v1/contactos")
async def get_contactos():
    # TODO read contactos.csv
    # TODO JSON encode contactos.csv
    # TODO Guardar en response
    response = []
    return response

