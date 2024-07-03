import streamlit as st

# Crear el menú de navegación en la barra lateral
st.sidebar.title('Inicio - Menú de navegación')
st.sidebar.markdown('''
    - [¿Que es PyTrivia?](#que-es-pytrivia)
    - [¿Que necesitas para comenzar?](#que-necesitas-para-comenzar)
    - [Instrucciones basicas](#instrucciones-basicas)
    - [Niveles de dificultad](#niveles-de-dificultad)
    - [Datos de los desarrolladores](#datos-de-los-desarrolladores)
''')

st.title('Bienvenidos a PyTrivia')

# Breve descripción del juego
# Se agrega un elemento de anclaje justo antes del encabezado para "¿Que es PyTrivia?"
st.markdown('<a name="que-es-pytrivia"></a>', unsafe_allow_html=True)
st.header('¿Que es PyTrivia?')
st.write('''
    PyTrivia es un juego de preguntas y respuestas diseñado para desafiar tus 
    conocimientos en diferentes áreas. Cada partida te presenta una serie de 
    preguntas basadas en conjuntos de datos proporcionados por la cátedra. 
    Tu objetivo es responder correctamente la mayor cantidad de preguntas 
    posibles y obtener la mejor puntuación.
''')

# Datos necesarios para comenzar a jugar
st.markdown('<a name="que-necesitas-para-comenzar"></a>', unsafe_allow_html=True)
st.header('¿Que necesitas para comenzar?')
st.write('''
    Para comenzar a jugar a PyTrivia, necesitas lo siguiente:
    - Un usuario registrado.
    - Acceso a Internet.
    - Una computadora.
    - Ganas de aprender y divertirte.
    
    Si aún no tienes un usuario registrado, puedes dirigirte al apartado de 
    formulario antes de comenzar a jugar.
''')

# Instrucciones básicas para comenzar a jugar
st.markdown('<a name="instrucciones-basicas"></a>', unsafe_allow_html=True)
st.header('Instrucciones basicas')
st.write('''
    Para jugar a PyTrivia, sigue estos pasos:
    1. Elige un usuario o regístrate si es tu primera vez.
    2. Dirígete al apartado Juego
    3. En caso de que tu usuario se encuentre repetido, selecciona tu email 
       también.     
    4. Selecciona una temática y una dificultad.
    5. Responde las preguntas que se te presenten.
    6. ¡Diviértete y aprende!
''')

# Explicación del parámetro dificultad
st.markdown('<a name="niveles-de-dificultad"></a>', unsafe_allow_html=True)
st.header('Niveles de dificultad')
st.write('''
    PyTrivia ofrece tres niveles de dificultad:
    - Fácil: Se te brindan tres opciones de respuesta y una pista sobre la 
      respuesta correcta.
    - Media: Se te indica la cantidad de palabras que tiene la respuesta 
      correcta.
    - Alta: No se brindan ayudas, debes responder solo con tus conocimientos.
    Elige el nivel que mejor se adapte a ti y desafía tus habilidades.
''')

# Datos de los participantes
st.markdown('<a name="datos-de-los-desarrolladores"></a>', unsafe_allow_html=True)
st.header('Datos de los desarrolladores')
students = st.tabs(["1° Alumno", "2° Alumno", "3° Alumno", "4° Alumno"])

with students[0]:
    st.write('''
        ### Nombre: Dante Puddu \n
        ### Legajo: 21665/6 \n
        ### DNI: 45913150
    ''')

with students[1]:
    st.write('''
        ### Nombre: Tomas Zorzoli \n
        ### Legajo: 21269/7 \n
        ### DNI: 45284239
    ''')

with students[2]:
    st.write(''' 
        ### Nombre: Emanuel Salmeron \n
        ### Legajo: 21219/6 \n
        ### DNI: 45400320
    ''')

with students[3]:
    st.write('''
        ### Nombre: Juan Segobia \n
        ### Legajo: 19113/6 \n
        ### DNI: 43912027
    ''')
