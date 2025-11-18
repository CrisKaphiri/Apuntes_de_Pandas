# BASE DE DATOS PARA EJEMPLO DE ARCHIVO 01_crear_leer_guardar.ipynb

import sqlite3

# Crear archivo .db
conexion = sqlite3.connect("data/frutas.db")
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
               CREATE TABLE frutas (
                   id INTEGER PRIMARY KEY,
                   fruta TEXT,
                   color TEXT,
                   stock INTEGER
               )
               """)

# Insertar datos
cursor.execute(
    "INSERT INTO frutas (fruta, color, stock) VALUES ('Manzana', 'Rojo', 1000)"
)
cursor.execute(
    "INSERT INTO frutas (fruta, color, stock) VALUES ('Platano', 'Amarillo', 2000)"
)
cursor.execute(
    "INSERT INTO frutas (fruta, color, stock) VALUES ('Naranja', 'Naranjo', 3000)"
)

conexion.commit()
conexion.close()
