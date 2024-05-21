import streamlit as st  
import json  
import pathlib

def ranking(values: dict):
    if 'results' not in st.session_state:
        st.session_state["results"] = {}  # Si no existe, lo inicializamos como un diccionario vacío
    
    # Cargar datos de usuarios desde el archivo si existe
    ruta = pathlib.Path("./data_users/results.json")
    if ruta.exists():
        with open(ruta, "r") as f:
            try:
                st.session_state["results"] = json.load(f)
            except json.JSONDecodeError:
                # Si hay un error al cargar el archivo (por estar vacío o tener un formato incorrecto), inicializamos como un diccionario vacío
                st.session_state["results"] = {}
    
    # Guardar los datos de usuarios
    st.session_state["results"][values.get('email')] =  {
        "username": values.get('username'),
        "score": values.get('score'),
        "difficulty": values.get('difficulty'),
        "theme": values.get('theme'),
        "gender": values.get('gender')
    }
    
    # Guardar los datos de usuarios en el archivo
    with open(ruta, "w") as f:
        json.dump(st.session_state["results"], f, indent=4)
