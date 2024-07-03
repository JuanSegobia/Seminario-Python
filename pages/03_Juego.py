import streamlit as st
import pathlib
import pandas as pd
import json
import random
from datetime import date
from resources import crafting_ranking as craft
from resources.validations import validar, exceptions

st.title('Bienvenido a PyTrivia!')

# Cargamos el archivo JSON
with open('./data_users/users.json', 'r') as file:
    data = json.load(file)

if data != {}:
    st.subheader('Antes de empezar, tienes usuario?')

    if st.button('No, quiero registrarme!!'):
        # Redirigir a la página de formulario
        st.switch_page("./pages/04_Formulario.py")

    st.subheader('Ingrese los datos de tu usuario:')

    # Extraemos los nombres de usuario y asociamos correos electrónicos
    users_emails = {}
    for email, user in data.items():
        if user['username'] not in users_emails:
            users_emails[user['username']] = []
        users_emails[user['username']].append(email)

    # Extraemos los nombres de usuario únicos
    user_names = list(users_emails.keys())

    # Widget selectbox para seleccionar un nombre de usuario
    selected_name = st.selectbox('Selecciona un nombre de usuario:', user_names)

    # Mostrar correos electrónicos asociados si hay más de uno
    associated_emails = users_emails[selected_name]
    if len(associated_emails) > 1:
        selected_email = st.selectbox('Selecciona un correo electrónico:', associated_emails)
    else:
        selected_email = associated_emails[0]

    # Lista de temáticas disponibles
    themes_to_select = ['Lagos', 'Aeropuertos', 'Conectividad', 'Censo 2022']

    # Widget selectbox para seleccionar una temática
    selected_theme = st.selectbox('Selecciona una temática:', themes_to_select)

    # Tupla con dificultades
    difficulties = ('Facil', 'Media', 'Dificil')

    # Widget para elegir la dificultad
    selected_difficulty = st.selectbox('Selecciona una dificultad:', difficulties)

    # Guardo los paths de los datasets
    paths = {
        'Aeropuertos': './custom_datasets/processed_airports.csv',
        'Lagos': './custom_datasets/lagos_arg.csv',
        'Conectividad': './custom_datasets/Conectividad_Internet.csv',
        'Censo 2022': './custom_datasets/c2022_tp_c_resumen_adaptado.csv'
    }

    # Guardo las columnas que se van a preguntar
    used_columns = {
        'Aeropuertos': ['Tipo de Aeropuerto', 'Nombre', 'Pies de Elevacion', 
                        'Tipo de Elevacion', 'Nombre de la Provincia'],
        'Lagos': ['Nombre', 'Ubicación', 'Superficie (km²)', 'Sup Tamaños'],
        'Conectividad': ['Provincia', 'Partido', 'Localidad', 'Poblacion', 'posee_conectividad'],
        'Censo 2022': [
            'Jurisdicción', 'Total de población', 'Población en viviendas particulares',
            'Población en viviendas colectivas (¹)', 'Población en situación de calle(²)',
            'Varones Total de población', 'Varones Población en viviendas particulares',
            'Varones Población en viviendas colectivas (¹)', 'VaronesPoblación en situación de calle(²)',
            'Mujeres Total de población', 'Mujeres Población en viviendas particulares',
            'Mujeres Población en viviendas colectivas (¹)', 'Mujeres Población en situación de calle(²)'
        ]
    }

    df = pd.read_csv(paths[selected_theme])
    columns = used_columns[selected_theme]

    # Pasamos todos los valores del dataframe a string.
    # Tenemos que pasarlo a string porque después compara un float con string.
    df = df.astype(str)

    # Los nombres de las columnas del dataset de aeropuertos estan en ingles.
    # Esto solo ocurre en el dataset de aeropuertos.
    # Renombrar las columnas en el DataFrame si la tematica es "Aeropuertos".
    if selected_theme == "Aeropuertos":
        df = df.rename(columns={
            'type': 'Tipo de Aeropuerto',
            'name': 'Nombre',
            'elevation_ft': 'Pies de Elevacion',
            'elevation_name': 'Tipo de Elevacion',
            'region_name': 'Nombre de la Provincia'
        })

    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
        st.session_state.confirmed = False

    if not st.session_state.game_started:
        if st.button('Comenzar a jugar'):
            st.session_state.questions = []  # Datos de la pregunta
            st.session_state.corrects_answers = []  # Respuestas correctas de cada pregunta
            st.session_state.user_answers = [None] * 5  # Respuestas del usuario
            st.session_state.game_started = True  # Variable para indicar si el juego comenzó
            st.session_state.confirmed = False
            st.session_state.show_results = False

            st.markdown('[Comenzar a jugar](#inicio-del-juego)')

            with st.sidebar:  # Sidebar con la información del usuario
                st.header('Datos de usuario')
                st.write('Nombre de usuario: ', selected_name)
                st.write('Tematica seleccionada: ', selected_theme)
                st.write('Dificultad seleccionada: ', selected_difficulty)

            for j in range(5):
                random_row = df.sample(n=1, replace=False)
                selected_columns = random.sample(columns, 4)  # Generamos 4 columnas random
                column_question, column_data1, column_data2, column_data3 = selected_columns

                if selected_difficulty == 'Facil':  # Generamos 2 respuestas falsas si la dificultad es fácil
                    exceptions(random_row, column_question, selected_theme)
                    options = [random_row[column_question].values[0]]
                    while len(options) < 3:
                        false_option = df.sample(n=1, replace=False)
                        exceptions(false_option, column_question, selected_theme)
                        if false_option[column_question].values[0] not in options:
                            options.append(false_option[column_question].values[0])
                    # Revolvemos la lista options para que la respuesta correcta no esté siempre primero
                    random.shuffle(options)

                st.session_state.questions.append({  # Guardamos los datos de la pregunta
                    'row': random_row,  # La fila de la pregunta
                    'column_question': column_question,  # Columna de la pregunta a responder
                    'column_data1': column_data1,  # Columnas de los datos a mostrar (clues)
                    'column_data2': column_data2,
                    'column_data3': column_data3
                })
                if selected_difficulty == 'Facil':
                    st.session_state.questions[j]['options'] = options

                # Excepciones para que el usuario pueda responder las preguntas sin la necesidad de agregar
                exceptions(random_row, column_question, selected_theme)

                # Agregamos la respuesta correcta
                st.session_state.corrects_answers.append(random_row[column_question].values[0])

    if st.session_state.game_started:
        st.markdown('<a name="inicio-del-juego"></a>', unsafe_allow_html=True)
        st.header('Inicio del juego')

        # Esta parte crea visualmente cada pregunta y guarda las respuestas
        for i, question in enumerate(st.session_state.questions):
            st.subheader(f'Pregunta {i + 1}:')
            random_row = question['row']
            column_question = question['column_question']
            column_data1 = question['column_data1']
            column_data2 = question['column_data2']
            column_data3 = question['column_data3']

            st.write(column_data1, ': ', random_row[column_data1].values[0])
            st.write(column_data2, ': ', random_row[column_data2].values[0])
            st.write(column_data3, ': ', random_row[column_data3].values[0])
            st.write(column_question, '= ??')
            match selected_difficulty:  # Depende de la dificultad como se piden las respuestas
                case 'Facil':
                    options = question['options']
                    st.session_state.user_answers[i] = st.radio(
                        f"Selecciona una opción para la pregunta {i + 1}:", options)
                case 'Media':
                    st.write(f'Pista: la respuesta tiene {len(str(st.session_state.corrects_answers[i]))} letras')
                    st.session_state.user_answers[i] = st.text_input(
                        f"Ingrese la respuesta correcta de la pregunta {(i + 1)}")
                case 'Dificil':
                    st.session_state.user_answers[i] = st.text_input(
                        f"Ingrese la respuesta correcta de la pregunta {(i + 1)}")

        if st.button('Confirmar respuestas'):
            st.session_state.confirmed = True
            user_answers = st.session_state.user_answers
            correct_answers = st.session_state.corrects_answers

            # Cantidad de respuestas correctas
            # Se juntan ambas listas con zip donde cada elemento contiene la respuesta correcta y la del usuario
            corrects = sum(
                1 for user_answers, correct_answers in zip(user_answers, correct_answers)
                if validar(user_answers) == validar(correct_answers)
            )

            st.session_state.points = corrects
            if selected_difficulty == 'Media':  # Se calculan la cantidad de puntos
                st.session_state.points = st.session_state.points * 2
            elif selected_difficulty == 'Dificil':
                st.session_state.points = st.session_state.points * 3

            st.session_state.game_started = False

            user_genre = data[selected_email]["gender"]

            parameters = {
                'username': selected_name, 'score': st.session_state.points,
                'email': selected_email, 'difficulty': selected_difficulty,
                'theme': selected_theme, 'gender': user_genre,
                'date': str(date.today()), 'incorrects': 5 - corrects
            }

            # Se llama al proceso que agrega al ranking este resultado
            craft.ranking(parameters)
            st.session_state.confirmed = False
            st.session_state.show_results = True
            st.switch_page("./pages/05_Ranking.py")
else:
    st.title("No hay datos para mostrar ya que no hay usuarios registrados.")
    if st.button('Registrarse'):
        st.switch_page("./pages/04_Formulario.py")
