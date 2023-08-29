import streamlit as st
import sqlite3

# Función para crear la tabla si no existe
def create_table():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS opciones (opcion TEXT)")
    conn.commit()
    conn.close()

# Función para añadir una opción a la tabla
def add_opcion(opcion):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO opciones (opcion) VALUES (?)", (opcion,))
    conn.commit()
    conn.close()

# Crear la tabla en la base de datos SQLite
create_table()

# Permitir al usuario seleccionar una opción
opcion_seleccionada = st.selectbox("Elige una opción:", ["Opción 1", "Opción 2", "Opción 3", "Opción 4"])

# Botón para registrar la selección
if st.button("Enviar"):
    add_opcion(opcion_seleccionada)
    st.write(f"Has seleccionado: {opcion_seleccionada}")
