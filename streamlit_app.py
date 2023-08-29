import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame de pandas
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Opcion"])

# Desplegar un selector con 4 opciones
opcion = st.selectbox("Elige una opción:", ["Opción 1", "Opción 2", "Opción 3", "Opción 4"])

# Botón para registrar la elección del usuario
if st.button("Enviar"):
    # Añadir la selección del usuario al DataFrame
    new_row = {"Opcion": opcion}
    df = df.append(new_row, ignore_index=True)
    # Guardar el DataFrame en el archivo CSV
    df.to_csv("data.csv", index=False)

# Crear y mostrar un gráfico de barras basado en las selecciones
st.subheader("Resultados")
df["Opcion"].value_counts().plot(kind="bar")
plt.xlabel("Opciones")
plt.ylabel("Número de selecciones")
plt.title("Selecciones de los usuarios")
st.pyplot()

