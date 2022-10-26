import streamlit as st
import pandas as pd
import numpy as np

st.write("""
#Hola de nuevo
Hola :V
""")
st.title('Hola xD')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

st.map(df)
