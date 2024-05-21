import json
import pandas as pd
import streamlit as st

st.header('| Este es el ranking de usuarios |')

# Cargar los datos del archivo JSON
with open('./data_users/results.json', 'r') as file:
    data = json.load(file)

# Convertir los datos a un DataFrame sin usar las claves como índice
df = pd.DataFrame(data.values())

# Asegurarse de que el campo 'score' sea numérico
df['score'] = pd.to_numeric(df['score'])

# Añadir la columna 'email' desde las claves del diccionario original
df['email'] = list(data.keys())

# Ordenar los datos por 'score' en orden descendente
df = df.sort_values(by='score', ascending=False)

# Tomar los primeros 15 registros
df_top_15 = df.head(15)

# Añadir la columna de posición
df_top_15['Posición'] = range(1, len(df_top_15) + 1)

# Reorganizar las columnas para que 'posición' sea la primera
df_top_15 = df_top_15[['Posición', 'username', 'score', 'email']]

# Mostrar la tabla en Streamlit sin el índice
st.write(df_top_15.reset_index(drop=True).to_html(index=False), unsafe_allow_html=True)