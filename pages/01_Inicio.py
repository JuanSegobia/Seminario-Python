import streamlit as st

def main():
    # Crear el menú de navegación en la barra lateral
    st.sidebar.title('Menú de navegación')
    st.sidebar.markdown('''
        - [Bienvenida](#bienvenida)
        - [¿Que es PyTrivia?](#que-es-pytrivia)
        - [¿Que necesitas para comenzar?](#que-necesitas-para-comenzar)
        - [Instrucciones basicas](#instrucciones-basicas)
        - [Niveles de dificultad](#niveles-de-dificultad)
        - [Datos de los participantes](#datos-de-los-participantes)
    ''')

    st.title('Bienvenidos a PyTrivia')

    # Sección de bienvenida
    st.header('Bienvenida')
    st.write('''
        Bienvenido a PyTrivia
    ''')

    # Breve descripción del juego

    # Se agrega un elemento de anclaje justo antes del encabezado para "¿Que es PyTrivia?"
    # Esto se hace para permitir la navegación mediante enlaces desde el menú de navegación lateral ya que al tener signos de pregunta no se redirige bien de la otra forma.
    st.markdown('<a name="que-es-pytrivia"></a>', unsafe_allow_html=True) 
    st.header('¿Que es PyTrivia?')
    st.write('''
        Breve descripción del juego.

    ''')

    # Datos necesarios para comenzar a jugar

    # Se agrega un elemento de anclaje justo antes del encabezado para "¿Que necesitas para comenzar?"
    # Esto se hace para permitir la navegación mediante enlaces desde el menú de navegación lateral ya que al tener signos de pregunta no se redirige bien de la otra forma.
    st.markdown('<a name="que-necesitas-para-comenzar"></a>', unsafe_allow_html=True)
    st.header('¿Que necesitas para comenzar?')
    st.write('''
        Datos necesarios para comenzar a jugar.

    ''')

    # Instrucciones básicas para comenzar a jugar
    st.header('Instrucciones basicas')
    st.write('''
        Instrucciones básicas para hacerlo comenzar a jugar.

    ''')

    # Explicación del parámetro dificultad
    st.header('Niveles de dificultad')
    st.write('''
        Explicación del funcionamiento del parámetro dificultad en el juego.
    ''')

    # Datos de los participantes
    st.header('Datos de los participantes')
    participante_tabs = st.tabs(["Participante 1", "Participante 2", "Participante 3", "Participante 4"])

    with participante_tabs[0]:
        st.write('''
            ### Nombre: Dante Puddu \n
            ### Legajo: 21665/6 \n
            ### DNI: 45913150
        ''')
    
    with participante_tabs[1]:
        st.write('''
            ### Nombre: Tomas Zorzoli \n
            ### Legajo: 21269/7 \n
            ### DNI: 45284239
        ''')
    
    with participante_tabs[2]:
        st.write(''' 
            ### Nombre: Emanuel Salmeron \n
            ### Legajo: 21219/6 \n
            ### DNI: 45400320
        ''')
    
    with participante_tabs[3]:
        st.write('''
            ### Nombre: Juan Segobia \n
            ### Legajo: 19113/6 \n
            ### DNI: 43912027
        ''')

if __name__ == "__main__":
    main()
