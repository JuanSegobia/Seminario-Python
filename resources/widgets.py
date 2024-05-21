import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import geopandas as gpd

def airport_map(dfa):
    # Configurar el título de la aplicación en Streamlit
    st.title('Datos Interesantes')

    st.subheader('Mapa de aeropuertos segun su elevacion:')
    st.write('🟢 Elevacion Baja')
    st.write('🟡 Elevacion Media')
    st.write('🔴 Elevacion Alta')
    st.write('⚫ Elevacion Desconocida')

    # Crear una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))

    # Diccionario para acceder a los colores correspondientes
    colores = {'alto': 'red', 'medio': 'yellow', 'bajo': 'green', 'Desconocido': 'black'}

    for index, row in dfa.iterrows():  # Recorro el dataframe por lineas
        color = colores[row['elevation_name']]  # Guardo en la variable el color que tengo que usar pasandole la elevacion como indice al diccionario
        ax.scatter(row['longitude_deg'], row['latitude_deg'], color=color, s=10, alpha=0.6)
    # Se podria hacer creando otra columna al dataframe que tenga el color que va a usar

    # Limito los valores de las coordenadas que se pueden ver en el mapa para que solamente muestre la zona de argentina
    ax.set_xlim([-80, -45])
    ax.set_ylim([-58, -18])

    # Configurar etiquetas y títulos
    ax.set_title('Mapa de aeropuertos segun su elevacion')
    ax.set_xlabel('Longitud')
    ax.set_ylabel('Latitud')

    # Añadir el gráfico a la aplicación de Streamlit
    st.pyplot(fig)

def lake_sizes(dfl):
    st.subheader('Grafico de barras de los tamaños de los lagos:')

    values = dfl['Sup Tamaños'].value_counts().values
    labels = dfl['Sup Tamaños'].value_counts().index

    fig, ax = plt.subplots()  # Creamos una nueva figura
    ax.bar(labels, values)  # Crear el gráfico de barras en la nueva figura

    # Agregar etiquetas y título
    ax.set_xlabel('Tamaño del lago')
    ax.set_ylabel('Cantidad')
    ax.set_title('Cantidad de lagos por tamaño')

    # Rotar etiquetas en el eje x para mejor legibilidad
    plt.xticks(rotation=45)

    # Mostrar el gráfico de barras
    st.pyplot(fig)

def airports_types(dfa):

    # Configurar el título de la aplicación en Streamlit
    st.subheader('Gráfico de torta con porcentaje de cada tipo de aeropuerto')

    # Crear una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 8))

    dfa_filtrado = dfa[dfa['type'] != 'closed']
    tipos = dfa_filtrado['type'].unique()
    cant_aeropuertos = dfa_filtrado['type'].value_counts()

    st.write(tipos)
    st.write(cant_aeropuertos)

    ax.pie(cant_aeropuertos, labels=tipos, autopct='%1.1f%%', labeldistance=1, pctdistance=0.8, startangle=250)

    ax.axis('equal')  # Para que el gráfico sea un círculo

    # Añadir el gráfico a la aplicación de Streamlit
    st.pyplot(fig)
    
def cant_airports(dfa):

    # Configuro el subtitulo para el grafico
    st.subheader('Mapa de provincias segun su cantidad de aeropuertos')

    # Creo una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(14, 26))

    # Creo una columna con todas las provincias de argentina y reemplazo la palabra province para que solo quede el nombre
    provincias = dfa['region_name'].str.replace('Province', '').unique()

    # Creo una columna con cada provincia y su cantidad de aeropuertos respectivamente
    cant_aeropuertos = dfa['region_name'].value_counts()

    # Creo el grafico de barras horizontal
    ax.barh(provincias, cant_aeropuertos)
    
    # Hago que la cantidad de aetopuertos tenga un espaciado de 25
    ax.set_xticks(range(0, cant_aeropuertos.max() + 25, 25))
    
    # Configuro los ejes y el titulo del grafico
    ax.set_xlabel('Aeropuertos')
    ax.set_ylabel('Provincias')
    ax.set_title('Gráfico de Barras de provincias segun su cantidad de aeropuertos')

    # Añado el gráfico a la aplicación de Streamlit
    st.pyplot(fig)

def graph_lakes(dfl):

    st.subheader('Mapa de superficie por km² de cada Lago')

    # Generar el gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(dfl['Nombre'], dfl['Superficie (km²)'], color='lightgreen')  # Cambia 'Nombre' y 'Superficie (km²)' si es necesario
    ax.set_title('Superficie de los Lagos')
    ax.set_xlabel('Superficie en km²')
    ax.set_ylabel('Lago')
    ax.tick_params(axis='y', labelsize=10)  # Ajustar el tamaño de las etiquetas del eje y
    ax.grid(True)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)


# Función para crear el mapa de los lagos
def lakes_map(dfl):
    # Configurar el título de la aplicación en Streamlit
    st.subheader('Mapa de ubicación de lagos en Argentina:')

    # Ruta al shapefile de Argentina
    argentina_shapefile = './shapefiles/ne_10m_admin_0_countries.shp'

    # Cargar el contorno de Argentina
    world = gpd.read_file(argentina_shapefile)
    argentina = world[world['ADMIN'] == 'Argentina']

    # Crear una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 10))

    # Graficar el contorno de Argentina
    argentina.boundary.plot(ax=ax, linewidth=1, edgecolor='black')

    # Graficar los puntos de los lagos
    ax.scatter(dfl['Longitud'], dfl['Latitud'], color="blue", s=10, alpha=0.6)

    # Limitar los valores de las coordenadas para mostrar solo la zona de Argentina
    # Usar los límites geográficos de Argentina para establecer los límites de los ejes
    ax.set_xlim(argentina.total_bounds[0], argentina.total_bounds[2])
    ax.set_ylim(argentina.total_bounds[1], argentina.total_bounds[3])

    # Configurar etiquetas y títulos
    ax.set_title('Mapa de lagos en Argentina')
    ax.set_xlabel('Longitud')
    ax.set_ylabel('Latitud')

    # Añadir el gráfico a la aplicación de Streamlit
    st.pyplot(fig)