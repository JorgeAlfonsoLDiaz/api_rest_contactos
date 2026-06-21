import requests

URI = "API_Ejemplo"

response = requests.get(URI)

print(f"GET : {response.text}")
print(f"GET : {response.status_code}")

# --------------------------------------------

data = {
        "id_contactos":5,
        "nombre":"Demo",
        "primer_apellido":"Demo1",
        "segundo_apellido":"Demo2",
        "email":"demo@email.com",
        "telefono":"1234567890"
       }
response = requests.post(URI, json=data)

print(f"POST : {response.text}")
print(f"POST : {response.status_code}")
