import pandas as pd
import json
import pathlib
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
import calendar

# Ruta del archivo JSON
route = pathlib.Path("./data_users/results.json")

# Elimina warning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Data variable global
with open(route, 'r') as f:
    data = json.load(f)

#------------------------------------------ Inciso 1 --------------------------------------------------------

def user_gender(df: pd.DataFrame):
    """ Genera y muestra un gráfico de torta que representa la distribución de género de usuarios únicos
        a partir de datos en un archivo JSON. """

    st.subheader('Usuarios por Género: ')

    # Eliminar usuarios duplicados(uso el mail que es unico)
    df = df.drop_duplicates(subset='mail')

    # Contar la cantidad de usuarios por género
    user_gender_counts = df['gender'].value_counts()

    # Graficar el gráfico de torta de usuarios por género
    plt.figure(figsize=(8, 6))
    plt.pie(user_gender_counts, labels=user_gender_counts.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.tight_layout()
    st.pyplot()

#------------------------------------------ Inciso 2 --------------------------------------------------------

def percentage_above_average_score(df: pd.DataFrame):
    """ Genera y muestra un gráfico de torta que representa el porcentaje de partidas con puntuaciones
        superiores y no superiores al promedio de puntajes de un conjunto de datos en un archivo JSON. """

    st.subheader('Porcentaje de partidas respecto al promedio de puntajes: ')

    # Calcular el promedio de calificaciones
    average_score = df['score'].mean()

    # Contar la cantidad de partidas con puntuación superior a la media
    above_average_count = (df['score'] > average_score).sum()

    # Contar la cantidad de partidas con puntuación inferior o igual a la media
    below_equal_average_count = len(df) - above_average_count

    # Graficar el gráfico de torta con el porcentaje de partidas por encima y por debajo de la media
    plt.figure(figsize=(8, 6))
    plt.pie([above_average_count, below_equal_average_count], labels=['Arriba del Promedio', 'Igual o Debajo del Promedio'], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.tight_layout()
    st.pyplot()

#------------------------------------------ Inciso 3 --------------------------------------------------------

def matchs_per_day(df: pd.DataFrame):
    '''Muestra en streamlit la cantidad de partidas realizadas por día de la semana en un gráfico de barras.'''

    st.subheader('Cantidad de partidas realizadas por día de la semana: ')

    # Convertir la columna 'fecha' a datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Filtrar filas con fechas inválidas
    df = df.dropna(subset=['date'])

    # Obtener el día de la semana para cada fecha
    df['day_of_the_week'] = df['date'].dt.day_name()

    # Contar la cantidad de partidas para cada día de la semana
    games_per_day = df['day_of_the_week'].value_counts().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], fill_value=0)

    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    games_per_day.plot(kind='bar', ax=ax, color='skyblue')

    # Configurar etiquetas y títulos
    ax.set_xlabel('Día de la semana')
    ax.set_ylabel('Cantidad de partidas')

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

#------------------------------------------ Inciso 4 --------------------------------------------------------

def average_correct_answers_per_month(df: pd.DataFrame):
    '''Muestra en streamlit el promedio de preguntas acertadas por mes entre dos fechas ingresadas.'''

    # Pido que ingrese las fechas a comparar
    first_date = st.date_input('Ingrese la primera fecha:', min_value=datetime(1924, 1, 1), max_value=datetime.now())
    second_date = st.date_input('Ingrese la segunda fecha:', min_value=datetime(1924, 1, 1), max_value=datetime.now())

    if first_date and second_date:
        if first_date > second_date:
            first_date, second_date = second_date, first_date  # por lo tanto, si es mayor, las intercambio

        # Convertir la columna 'date' a datetime si no está ya en ese formato
        if not pd.api.types.is_datetime64_any_dtype(df['date']):
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df = df.dropna(subset=['date'])

        # Filtrar datos dentro del rango de fechas
        mask = (df['date'] >= pd.to_datetime(first_date)) & (df['date'] <= pd.to_datetime(second_date))
        df_filtered = df.loc[mask].copy()

        if df_filtered.empty:
            st.warning("No hay datos en el rango de fechas seleccionado.")
            return

        # Agrupar por mes y calcular el promedio de preguntas correctas
        df_filtered['mes'] = df_filtered['date'].dt.to_period('M')
        promedio_aciertos_mensuales = df_filtered.groupby('mes')['score'].mean()

        # Formatear el índice como nombres de meses
        promedio_aciertos_mensuales.index = promedio_aciertos_mensuales.index.strftime('%B %Y')

        # Mostrar los resultados
        st.write("Promedio de preguntas acertadas por mes entre las fechas seleccionadas:")
        st.write(promedio_aciertos_mensuales)

        # Gráfico de barras del promedio mensual
        fig, ax = plt.subplots()
        promedio_aciertos_mensuales.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_xlabel('Mes')
        ax.set_ylabel('Promedio de preguntas acertadas')
        ax.set_title('Promedio mensual de preguntas acertadas')
        plt.xticks(rotation=45)  # Rotar los nombres de los meses para mejor legibilidad
        st.pyplot(fig)


#------------------------------------------ Inciso 5 --------------------------------------------------------

def top10_users_between(df: pd.DataFrame):
    '''Muestra en streamlit los 10 usuarios registrados con mas puntos entre
    las 2 fechas seleccionadas en una tabla de forma descendente'''
    
    st.subheader('Top 10 usuarios por puntos entre 2 fechas ingresadas: ')
    
    # Pido que ingrese las fechas a comparar
    date1 = st.date_input('Ingrese la primera fecha:', min_value= datetime(1924, 1, 1), max_value= datetime.now(), key='date1')
    date2 = st.date_input('Ingrese la segunda fecha:', min_value= datetime(1924, 1, 1), max_value= datetime.now(), key='date2')
    
    # Me fijo si se ingresaron ambas fechas
    if date1 and date2 != "":
        dates_entered = True

    if st.button('confirmar ingreso') and dates_entered:
        if date1 > date2:  # Quiero que date1 sea la fecha menor y date2 la mayor,
            date1, date2 = date2, date1  # por lo tanto, si es mayor, las intercambio
        
        # Convierto la columna de fechas en objetos datetime
        df['date'] = pd.to_datetime(df['date']).dt.date
        
        # Filtro el dataframe para que queden los resultados que necesito
        df = df[(df['date'] > date1) & (df['date'] < date2)]
        
        # Guardo para cada mail su cantidad total de puntos, hago el rese_index() para convertir la variable a dataframe
        total_points = df.groupby('mail')['score'].sum().reset_index()
        
        # Ordeno el dataframe por puntaje de forma descentende, y dejo solamente los 10 mayores
        users_top_10 = total_points.sort_values(by='score', ascending=False).head(10)

        users_top_10.columns = ['Mail', 'Puntaje total']
        
        st.dataframe(users_top_10, hide_index=True)

#------------------------------------------ Inciso 6 --------------------------------------------------------

def hardest_datasets(df: pd.DataFrame):
    '''Muestra en streamlit una tabla de cada dataset con su
    cantidad de respuestas incorrectas ordenadas de forma descendente'''

    st.subheader('Datasets con mayor numero de errores: ')
    
    # Guardo en la variable cada tema con su cantidad de respuestas incorrectas
    incorrects_per_theme = df.groupby('theme')['incorrects'].sum().reset_index() # hago el .reset_index() para convertir la variable a dataframe

    # Ordeno el dataframe por su cantidad de respuestas incorrectas, de forma descendente
    incorrects_in_order = incorrects_per_theme.sort_values(by='incorrects', ascending=False)
    
    incorrects_in_order.columns = ['Dataset', 'Cant respuestas incorrectas']
    
    st.dataframe(incorrects_in_order, hide_index=True)
    
#------------------------------------------ Inciso 7 --------------------------------------------------------

def points_in_time(df: pd.DataFrame):
    ''' Comparara los puntos a traves del tiempo de dos usuarios, 
        devolviendo un grafico para cada usuario marcando fecha y dia. '''

    # Asegurarse de que la columna de fecha esté en el formato de fecha correcto
    df['date'] = pd.to_datetime(df['date'])

    # Extraer el mes y el año de la columna de fecha
    df['year_month'] = df['date'].dt.to_period('M')

    # Agrupar por usuario y por mes, y sumar los puntajes
    grouped = df.groupby(['username', 'year_month'])['score'].sum().reset_index()

    # Calcular el puntaje acumulado por usuario
    grouped['cumulative_score'] = grouped.groupby('username')['score'].cumsum()

    # Función para mostrar el gráfico en Streamlit
    def plot_scores_per_month(user):
        user_data = grouped[grouped['username'] == user]
        plt.figure(figsize=(10, 6))
        plt.plot(user_data['year_month'].astype(str), user_data['cumulative_score'], marker='o')
        plt.xlabel('Fecha')
        plt.ylabel('Puntaje Acumulado')
        plt.title(f'Puntaje Acumulado de {user} por Mes')
        plt.xticks(rotation=45)
        plt.ylim(0, user_data['cumulative_score'].max() + 1)
        st.pyplot(plt)

    # Interfaz de usuario en Streamlit
    st.subheader('Puntajes a traves del tiempo')

    # Seleccionar usuario
    selected_user1 = st.selectbox('Selecciona el primer usuario:', grouped['username'].unique())
    selected_user2 = st.selectbox('Selecciona el segundo usuario:', grouped['username'].unique())

    # Mostrar el gráfico para el usuario seleccionado
    if st.button('Confirmar Usuarios'):
        users_tabs = st.tabs([f"{selected_user1}", f"{selected_user2}"])

        with users_tabs[0]:
            st.subheader(f'Gráfico de líneas del usuario: {selected_user1}')
            plot_scores_per_month(selected_user1)

        with users_tabs[1]:
            st.subheader(f'Gráfico de líneas del usuario: {selected_user2}')
            plot_scores_per_month(selected_user2)

#------------------------------------------ Inciso 8 --------------------------------------------------------

def best_theme_by_gender(df: pd.DataFrame):
    ''' Calcula el puntaje promedio de cada tema, para cada genero y
        devuelve un cuadro con el tema en el que mas puntos se obtuvieron con cada genero'''

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

    st.subheader("Para cada genero, la tematica en la cual demuestra mayor conocimiento y su puntaje promedio:")
    
    st.write(results)

#------------------------------------------ Inciso 9 --------------------------------------------------------

def average_difficulty(df: pd.DataFrame):
    '''
    Funcion para calcular el promedio de puntajes por nivel de dificultad
    '''

    # Calcular la cantidad de veces que se eligio cada nivel de dificultad
    count_difficulty = df['difficulty'].value_counts()

    # Calcular el promedio de puntajes para cada nivel de dificultad
    average_score = df.groupby('difficulty')['score'].mean()

    # Mostrar los resultados de la cantidad de veces que se eligio cada nivel 
    # de dificultad y el promedio de puntajes para cada uno
    st.subheader("Cantidad de veces que se eligio cada dificultad:")

    st.write(count_difficulty)

    st.subheader("\nPromedio en puntos de cada dificultad:")

    st.write(average_score)

#------------------------------------------ Inciso 10 --------------------------------------------------------

def user_streak(df: pd.DataFrame):
    '''Muestra en streamlit los usuarios que han jugado al menos una partida en los últimos 7 días consecutivos.'''

    st.subheader('Listado de usuarios en racha de 7 dias: ')
    
    # Convertir la columna 'fecha' de string a datetime.date
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    # Obtener la fecha actual y la fecha límite (hace 7 días)
    current_date = datetime.now().date()
    date_limit = current_date - timedelta(days=7)
    
    # Filtrar las sesiones realizadas en los últimos 7 días
    recent_sessions = df[df['date'] >= date_limit]
    
    # Generar una lista con las fechas de los últimos 7 días
    dates_last_7_days = [date_limit + timedelta(days=i) for i in range(7)]
    
    # Crear un diccionario para contar las fechas por usuario
    date_count = {user: set() for user in recent_sessions['username'].unique()}
    
    # Llenar el diccionario con las fechas de sesiones por usuario
    for _, row in recent_sessions.iterrows():
        date_count[row['username']].add(row['date'])
    
    # Identificar los usuarios que tienen sesiones en cada uno de los últimos 7 días
    consistent_users = [user for user, dates in date_count.items() if all(date in dates for date in dates_last_7_days)]    
    df = pd.DataFrame(consistent_users, columns=['Usuarios'])

    st.dataframe(df,hide_index=True)