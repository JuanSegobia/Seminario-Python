import streamlit as st  
import pathlib
import pandas as pd
import json
import random
from resources import crafting_ranking as craft

st.header('Bienvenido a PyTrivia!')
st.subheader('Para empezar ingrese su usuario:')

# Cargamos el archivo JSON
with open('./data_users/users.json', 'r') as file:
    data = json.load(file)

# Extraemos los nombres de usuario y asociamos correos electrónicos
usuarios_emails = {}
for email, usuario in data.items():
    if usuario['username'] not in usuarios_emails:
        usuarios_emails[usuario['username']] = []
    usuarios_emails[usuario['username']].append(email)

# Extraemos los nombres de usuario únicos
nombres_usuarios = list(usuarios_emails.keys())

# Widget selectbox para seleccionar un nombre de usuario
nombre_seleccionado = st.selectbox('Selecciona un nombre de usuario:', nombres_usuarios)

# Mostrar correos electrónicos asociados si hay más de uno
emails_asociados = usuarios_emails[nombre_seleccionado]
if len(emails_asociados) > 1:
    email_seleccionado = st.selectbox('Selecciona un correo electrónico:', emails_asociados)
else:
    email_seleccionado = emails_asociados[0]

# Lista de temáticas disponibles
tematicas = ['Aeropuertos', 'Lagos', 'Conectividad', 'Censo 2022']

# Widget selectbox para seleccionar una temática
tematica_seleccionada = st.selectbox('Selecciona una temática:', tematicas)

# Tupla con dificultades
Dificultades = ('Facil', 'Media', 'Dificil')

# Widget para elegir la dificultad
dif_seleccionada = st.selectbox('Selecciona una dificultad:', Dificultades)

paths = {'Aeropuertos': './custom_datasets/processed_airports.csv',
         'Lagos': './custom_datasets/lagos_arg.csv',
         'Conectividad': './custom_datasets/Conectividad_Internet.csv',
         'Censo 2022': './custom_datasets/c2022_tp_c_resumen_adaptado.csv'}

columnas_usadas = {'Aeropuertos': ['type', 'name', 'elevation_ft', 'elevation_name', 'region_name'],
                   'Lagos': ['Nombre', 'Ubicación', 'Superficie (km²)', 'Sup Tamaños'],
                   'Conectividad': ['Provincia', 'Partido', 'Localidad', 'Poblacion', 'posee_conectividad'],
                   'Censo 2022': ['Jurisdicción', 'Total de población', 'Población en viviendas particulares', 'Población en viviendas colectivas (¹)',
                                  'Población en situación de calle(²)', 'Varones Total de población', 'Varones Población en viviendas particulares',
                                  'Varones Población en viviendas colectivas (¹)', 'VaronesPoblación en situación de calle(²)', 'Mujeres Total de población',
                                  'Mujeres Población en viviendas particulares', 'Mujeres Población en viviendas colectivas (¹)', 'Mujeres Población en situación de calle(²)',
                                  'Porcentaje de poblacion en situacion de calle']
                   }

df = pd.read_csv(paths[tematica_seleccionada])
columnas = columnas_usadas[tematica_seleccionada]

if 'juego_comenzado' not in st.session_state:
    st.session_state.juego_comenzado = False
    st.session_state.preguntas = []
    st.session_state.respuestas_correctas = []
    st.session_state.respuestas_usuario = [None] * 5
    st.session_state.se_confirmo = False


if not st.session_state.juego_comenzado:
    if st.button('Comenzar a jugar'):
        st.session_state.juego_comenzado = True
        
        for j in range(5):
            fila_random = df.sample(n=1, replace=False)
            columnas_seleccionadas = random.sample(columnas, 4)
            columna_a_encontrar, columna_dato1, columna_dato2, columna_dato3 = columnas_seleccionadas
            
            if dif_seleccionada == 'Facil':
                opciones = [fila_random[columna_a_encontrar].values[0]]
                while len(opciones) < 3:
                    opcion_falsa = df.sample(n=1, replace=False)
                    if opcion_falsa[columna_a_encontrar].values[0] not in opciones:
                        opciones.append(opcion_falsa[columna_a_encontrar].values[0])
                random.shuffle(opciones)    
                
            st.session_state.preguntas.append({
                'fila': fila_random,
                'columna_a_encontrar': columna_a_encontrar,
                'columna_dato1': columna_dato1,
                'columna_dato2': columna_dato2,
                'columna_dato3': columna_dato3
            })
            if dif_seleccionada == 'Facil':
                st.session_state.preguntas[j]['opciones'] = opciones
                
            st.session_state.respuestas_correctas.append(fila_random[columna_a_encontrar].values[0])

if st.session_state.juego_comenzado:
    for i, pregunta in enumerate(st.session_state.preguntas):
        st.subheader(f'Pregunta {i+1}:')
        fila_random = pregunta['fila']
        columna_a_encontrar = pregunta['columna_a_encontrar']
        columna_dato1 = pregunta['columna_dato1']
        columna_dato2 = pregunta['columna_dato2']
        columna_dato3 = pregunta['columna_dato3']
        
        st.write(columna_dato1, ': ', fila_random[columna_dato1].values[0])
        st.write(columna_dato2, ': ', fila_random[columna_dato2].values[0])
        st.write(columna_dato3, ': ', fila_random[columna_dato3].values[0])
        st.write(columna_a_encontrar, '= ??')
        match dif_seleccionada:
            case 'Facil':
                opciones = pregunta['opciones']
                st.session_state.respuestas_usuario[i] = st.radio(f"Selecciona una opción para la pregunta {i+1}:", opciones)
            case 'Media':
                st.write(f'Pista: la respuesta tiene {len(str(st.session_state.respuestas_correctas[i]))} letras')
                st.session_state.respuestas_usuario[i] = st.text_input(f"Ingrese la respuesta correcta de la pregunta {(i+1)}")
            case 'Dificil':
                st.session_state.respuestas_usuario[i] = st.text_input(f"Ingrese la respuesta correcta de la pregunta {(i+1)}")
                
    if st.button('Confirmar respuestas'):
        st.session_state.se_confirmo = True
        respuestas_usuario = st.session_state.respuestas_usuario
        respuestas_correctas = st.session_state.respuestas_correctas
        
        # Cantidad de respuestas correctas

        puntaje = sum(1 for respuesta_usuario, respuesta_correcta in zip(respuestas_usuario, respuestas_correctas) if respuesta_usuario == respuesta_correcta)
        
        match dif_seleccionada: 
            case 'Facil':
                st.session_state.puntaje = puntaje
            case 'Medio':
                st.session_state.puntaje = puntaje * 2
            case 'Dificil':
                st.session_state.puntaje = puntaje * 3
        
        st.session_state.preguntas = []
        st.session_state.juego_comenzado = False

        genero_usuario = data[email_seleccionado]["gender"]

        parameters = {'username': nombre_seleccionado, 'score': st.session_state.puntaje,
                      'email': email_seleccionado, 'difficulty': dif_seleccionada,
                      'theme': tematica_seleccionada, 'gender': genero_usuario}

        craft.ranking(parameters)
    
if st.session_state.se_confirmo:
    if st.button("Ir al ranking"):
        st.session_state.se_confirmo = False
        st.switch_page("./pages/05_Ranking.py")