import mysql.connector

import os
from dotenv import load_dotenv
load_dotenv()

# Establecer conexión
mydb = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DB")
)

# Crear un cursor
mycursor = mydb.cursor()


#INSERT
sql = "INSERT INTO clientes (id, nombre, apellido, email) VALUES (%s, %s, %s, %s)"
valores = ("20", "Pepe", "Betoben", "PeBete@yahoot.mlv")
mycursor.execute(sql, valores)
mydb.commit()

#DELETE
nombre = input("Elige el nombre que quieres eliminar: ")
sql = f"DELETE FROM clientes WHERE nombre = \"{nombre}\""
mycursor.execute(sql)
mydb.commit()

#SELECT
mycursor.execute("SELECT * FROM clientes")
resultados = mycursor.fetchall()
for fila in resultados:
    print(fila)


# Cerrar conexión
mydb.close()