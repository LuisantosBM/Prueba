import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# Carga de datos existentes (si los hay)
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Nombre", "Respuesta"])

# Pregunta e ingreso de nombre
nombre = st.text_input("Ingresa tu nombre:")
respuesta = st.selectbox("Selecciona una respuesta:", ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5"])

# Botón para enviar
if st.button("Enviar"):
    # Añadir nueva fila al DataFrame
    new_row = {"Nombre": nombre, "Respuesta": respuesta}
    df = df.append(new_row, ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv("data.csv", index=False)

# Reservar un espacio para la gráfica
placeholder = st.empty()

# Actualizar la gráfica en tiempo real
while True:
    # Leer los datos
    df = pd.read_csv("data.csv")
    
    # Crear la gráfica de barras
    fig, ax = plt.subplots()
    df["Respuesta"].value_counts().plot(kind='bar', ax=ax)
    ax.set_title("Respuestas en tiempo real")
    
    # Mostrar la gráfica en el espacio reservado
    placeholder.pyplot(fig)
    
    # Pausa antes de actualizar
    time.sleep(2)

