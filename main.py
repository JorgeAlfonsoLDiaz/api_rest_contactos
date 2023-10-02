import csv
import json

from typing import Union

from fastapi import FastAPI

app = FastAPI()


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
    response = json.dumps(response, indent=4)
    return response

