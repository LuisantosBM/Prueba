import streamlit as st

# Permitir al usuario seleccionar una opción
opcion_seleccionada = st.selectbox("Elige una opción:", ["Opción 1", "Opción 2", "Opción 3", "Opción 4"])

# Botón para registrar la selección
if st.button("Enviar"):
    st.write(f"Has seleccionado: {opcion_seleccionada}")
