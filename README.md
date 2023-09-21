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
´´´sql
CREATE TABLE ...
´´´
