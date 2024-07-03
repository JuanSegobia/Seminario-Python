import json
import pandas as pd
import streamlit as st
from resources.validations import validar

# Verificar si se deben mostrar los resultados
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

if st.session_state.show_results:

    st.subheader('Resultado de la última partida:')

    for i, questions in enumerate(st.session_state.questions):
        fila_random = questions['row']
        column_question = questions['column_question']
        column_data1 = questions['column_data1']
        column_data2 = questions['column_data2']
        column_data3 = questions['column_data3']
        
        st.subheader(f'Pregunta {i + 1}:')
        st.write(f'{column_data1}: {fila_random[column_data1].values[0]}')
        st.write(f'{column_data2}: {fila_random[column_data2].values[0]}')
        st.write(f'{column_data3}: {fila_random[column_data3].values[0]}')
        st.write(f'{column_question} = ??')
        
        if validar(st.session_state.corrects_answers[i]) == validar(st.session_state.user_answers[i]):
            st.success(f'Se respondió: {st.session_state.user_answers[i]}')
        else:
            st.error(f'Se respondió: {st.session_state.user_answers[i]} | La respuesta correcta era: {st.session_state.corrects_answers[i]}')

    st.subheader(f'El puntaje fue de: {st.session_state.points}')

# Cargar los datos del archivo JSON
results_file_path = './data_users/results.json'
with open(results_file_path, 'r') as file:
    data = json.load(file)

if data:
    st.header('| Top 15 mejores partidas |')

    # Convertir los datos a un DataFrame
    df = pd.DataFrame(data)

    # Asegurarse de que el campo 'score' sea numérico
    df['score'] = pd.to_numeric(df['score'])

    # Añadir la columna 'email' desde los datos originales
    df['email'] = [user['mail'] for user in data]

    # Ordenar los datos por 'score' en orden descendente
    df_sorted = df.sort_values(by='score', ascending=False)

    # Tomar los primeros 15 registros
    df_top_15 = df_sorted.head(15).copy()

    # Añadir la columna de posición
    df_top_15['Posición'] = range(1, len(df_top_15) + 1)

    # Reorganizar las columnas para que 'Posición' sea la primera
    df_top_15 = df_top_15[['Posición', 'username', 'score', 'email']]

    # Mostrar la tabla en Streamlit sin el índice
    st.write(df_top_15.reset_index(drop=True).to_html(index=False), unsafe_allow_html=True)
else:
    st.title("No hay datos para mostrar ya que no se ha jugado ninguna partida.")
