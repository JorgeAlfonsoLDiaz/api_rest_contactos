# Design Document: API REST CONTACTOS

## 1. Descripción
Ejemplo de una API REST para gestionar contactos en una DB utilizando FastAPI.


## 2. Objetivo
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framework [FastAPI](https://fastapi.tiangolo.com/).

## 3. Diseño de la BD
Para este ejemplo se utilizará el gestor de bases de datos [SQLite3](https://sqlite.org) con las siguientes tablas:

### 3.1 Tabla: contactos

|No.|Campo|Tipo|Restricciones|Descripción|
|--|--|--|--|--|
|1|id_contactos|int|PRIMARY KEY|Llave primaria de la tabla|

### 3.2 Script
```sql
CREATE TABLE ...
```

## 4. Diseño de la API

### 4.1 GET - http://localhost:8000/


|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Endpoint raíz de la API.|
|2|Summary|Endpoint raíz.|
|3|Method|GET|
|4|Endpoint|http://localhost:8000/|
|5|Query Param|NA|
|6|Path Param|NA|
|7|Data|NA|
|8|Version|v1|
|9|Status Code|200-OK|
|10|Response type|application/json|
|11|Response|{"version":"v1","message":"Endpointraíz","datetime":"21/09/2023 10:16"}|
|12|curl|curl -x 'GET' 'http://localhost:8000/' -H 'accept:application/json'|
|13|Status Code (error)|NA|
|14|Response type (error)|NA|
|15|Response (error)|NA|


### 4.2 GET - http://localhost:8000/contactos


|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Endpoint para consultar datos de la API.|
|2|Summary|Endpoint para consulta.|
|3|Method|GET|
|4|Endpoint|http://localhost:8000/contactos|
|5|Query Param|id_contacto|
|6|Path Param|NA|
|7|Data|NA|
|8|Version|v1|
|9|Status Code|200-OK|
|10|Response type|application/json|
|11|Response|{"version":"v1","message":"Consultar contactos","datetime":"25/09/2023 10:04"}|
|12|curl|curl -x 'GET' 'http://localhost:8000/contactos' -H 'accept:application/json'|
|13|Status Code (error)|400-Bad Request, 404-Not Found|
|14|Response type (error)|application/json|
|15|Response (error)|{"error":"Error al realizar la consulta"}|


### 4.3 POST - http://localhost:8000/contactos


|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Endpoint para enviar datos a la API.|
|2|Summary|Endpoint para enviar datos.|
|3|Method|POST|
|4|Endpoint|http://localhost:8000/contactos|
|5|Query Param|NA|
|6|Path Param|NA|
|7|Data|{"id_contacto":int,"nombre":string,"primer_apellido":string,"segundo_apellido":string,"email":string,"telefono":string}|
|8|Version|v1|
|9|Status Code|200-OK, 201-Created|
|10|Response type|application/json|
|11|Response|{"version":"v1","message":"Registro capturado","datetime":"25/09/2023 10:25"}|
|12|curl|curl -x 'POST' 'http://localhost:8000/contactos' -H 'accept:application/json'|
|13|Status Code (error)|400-Bad Request|
|14|Response type (error)|application/json|
|15|Response (error)|{"error":"No se pudo insertar el registro"}|


### 4.4 DELETE - http://localhost:8000/contactos


|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Endpoint para eliminar datos de la API.|
|2|Summary|Endpoint para eliminar.|
|3|Method|DELETE|
|4|Endpoint|http://localhost:8000/contactos/?id_contacto=|
|5|Query Param|NA|
|6|Path Param|{id_contacto}|
|7|Data|NA|
|8|Version|v1|
|9|Status Code|200-OK|
|10|Response type|application/json|
|11|Response|{"version":"v1","message":"Eliminado con éxito","datetime":"25/09/2023 10:53"}|
|12|curl|curl -x 'DELETE' 'http://localhost:8000/contactos' -H 'accept:application/json'|
|13|Status Code (error)|400-Bad Request, 404-Not Found|
|14|Response type (error)|application/json|
|15|Response (error)|{"error":"Error al eliminar"}|


### 4.5 PUT - http://localhost:8000/contactos


|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Endpoint para actualizar datos de la API.|
|2|Summary|Endpoint para actualizar.|
|3|Method|PUT|
|4|Endpoint|http://localhost:8000/contactos/?id_contacto=|
|5|Query Param|NA|
|6|Path Param|{id_contacto]|
|7|Data|{"id_contacto":int,"nombre":string,"primer_apellido":string,"segundo_apellido":string,"email":string,"telefono":string}|
|8|Version|v1|
|9|Status Code|200-OK|
|10|Response type|application/json|
|11|Response|{"version":"v1","message":"Actualizado correctamente","datetime":"25/09/2023 15:32"}|
|12|curl|curl -x 'PUT' 'http://localhost:8000/contactos' -H 'accept:application/json'|
|13|Status Code (error)|400-Bad Request, 404-Not Found|
|14|Response type (error)|application/json|
|15|Response (error)|{"error":"Error al actualizar"}|
