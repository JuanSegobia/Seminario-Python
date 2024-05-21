import pandas as pd
import json
import pathlib
import streamlit as st

# Ruta del archivo JSON
ruta = pathlib.Path("./data_users/results.json")

# Funcion para calcular el promedio de puntajes por nivel de dificultad
def average_difficulty():

    # Abrir el archivo JSON y cargar los datos en una variable
    with open(ruta, 'r') as f:
        data = json.load(f)

    # Crear un DataFrame a partir de los datos del archivo JSON
    df = pd.DataFrame.from_dict(data, orient='index')

    # Calcular la cantidad de veces que se eligio cada nivel de dificultad
    count_difficulty = df['difficulty'].value_counts()

    # Calcular el promedio de puntajes para cada nivel de dificultad
    average_score = df.groupby('difficulty')['score'].mean()

    # Mostrar los resultados de la cantidad de veces que se eligio cada nivel de dificultad y el promedio de puntajes para cada uno
    st.write("Cantidad de veces que se eligio cada dificultad:")

    st.write(count_difficulty)

    st.write("\nPromedio en puntos de cada dificultad:")

    st.write(average_score)


# Funcion para encontrar el tema con el puntaje promedio mas alto para cada genero
def best_theme_by_gender():
    # Abrir el archivo JSON y cargar los datos en una variable
    with open(ruta, 'r') as f:
        data = json.load(f)

    # Crear un DataFrame a partir de los datos del archivo JSON
    df = pd.DataFrame.from_dict(data, orient='index')

    # Calcular el puntaje promedio para cada combinacion de genero y tema
    average_score_by_gender_and_theme = df.groupby(['gender', 'theme'])['score'].mean()

    # Encontrar el tema con el puntaje promedio mas alto para cada genero
    best_theme_by_gender = average_score_by_gender_and_theme.groupby('gender').idxmax()

    # Obtener los puntajes promedio correspondientes a los temas seleccionados
    best_theme_scores = average_score_by_gender_and_theme.loc[best_theme_by_gender]

    # Crear un DataFrame con los resultados y mostrarlos
    results = pd.DataFrame({
        'Mejor tematica': [theme for gender, theme in best_theme_by_gender.values],
        'Puntaje promedio': best_theme_scores.values
    }, index=best_theme_by_gender.index)

    st.write("Para cada genero, la tematica en la cual demuestra mayor conocimiento y su puntaje promedio:")
    
    st.write(results)
