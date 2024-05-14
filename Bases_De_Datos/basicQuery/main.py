import mysql.connector

import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("MY_KEY"))

# Establecer conexión
mydb = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DB")
)

# Crear un cursor
mycursor = mydb.cursor()

# sql = "INSERT INTO clientes (id, nombre, apellido, email) VALUES (%s, %s, %s, %s)"
# valores = ("20", "Pepa", "Betoben", "PeBete@yahoot.mlv")
# mycursor.execute(sql, valores)
# mydb.commit()

# sql = "DELETE FROM clientes WHERE nombre = \"Pepe\""
# mycursor.execute(sql)
# mydb.commit()


# Ejecutar consulta
mycursor.execute("SELECT * FROM clientes")

# Obtener resultados
resultados = mycursor.fetchall()

# Iterar sobre los resultados
for fila in resultados:
    print(fila)

# Cerrar conexión
mydb.close()