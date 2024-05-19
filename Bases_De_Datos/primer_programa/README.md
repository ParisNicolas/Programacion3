# Primer programa
#### Trabajo Práctico N° 8
*Creación de una Aplicación Python conectada a una Base de Datos*

**Objetivo:** El objetivo de este proyecto es que cada estudiante realice la creación de la base de datos en Clever Cloud y el desarrollo de una aplicación en Python que se conecte a dicha base de datos. La base de datos ya ha sido diseñada en grupo, y ahora cada estudiante trabajará individualmente en la implementación de la misma en Clever Cloud y el desarrollo de la aplicación Python para consultas.

### Instalacion
1. Ejecuta el siguiente comando:
	`$ pip install mysql-connector-python dotenv-python`

2. Crea un archivo *.env*  en la misma carpeta con la siguiente informacion:
```text
HOST="url de la base de datos..."
USER="usuario..."
PASSWORD="contraseña..."
DB="nombre de la base de datos..."
```

### Explicación
Basicamente el codigo se conecta mediante python a una base de datos MySQL de CleverCloud y muestra una simple implemetacion de consultas INSERT, DELETE, SELECT:

- Primero inserta un registro en la entidad *clientes*
`INSERT INTO clientes (id, nombre, apellido, email) VALUES (%s, %s, %s, %s)`
- Luego elimina un fila de esta misma tabla, filtrado por el nombre a eleccion del usuario
`DELETE FROM clientes WHERE nombre = "{nombre}"`
- Por ultimo extrae todas las filas de la entidad *clientes*
`SELECT * FROM clientes`

El ciclo del programa se podria definir asi:
- Importacion de librerias (mysql-conector, dotenv)
- Obtencion de las variables de entorno
- Coneccion a la BD
- Consultas (INSERT, DELETE, SELECT): SQL query, ejecucion, commit/fetch
- Desconeccion con la BD