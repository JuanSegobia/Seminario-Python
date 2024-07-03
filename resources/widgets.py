import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import geopandas as gpd
from streamlit_folium import st_folium
import folium 

# ----------------------------------- Mapas aeropuertos -----------------------------------
def airport_map_geopandas(dfa: pd.DataFrame):
    '''Genera un mapa de los aeropuertos de Argentina según su elevación utilizando GeoPandas.'''
    # Ruta al shapefile de Argentina
    argentina_shapefile = './shapefiles/ne_10m_admin_0_countries.shp'

    # Crear una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(15, 15))
    
    # Cargar el contorno de Argentina
    world = gpd.read_file(argentina_shapefile)
    argentina = world[world['ADMIN'] == 'Argentina']
    
    # Graficar el contorno de Argentina
    argentina.boundary.plot(ax=ax, linewidth=1, edgecolor='black')
    
    # Diccionario para acceder a los colores correspondientes
    colors = {'alto': 'red', 'medio': 'yellow', 'bajo': 'green', 'Desconocido': 'black'}

    longitudes = dfa['longitude_deg'].values
    latitudes = dfa['latitude_deg'].values
    elevations = dfa['elevation_name'].values

    for lon, lat, elev in zip(longitudes, latitudes, elevations):
        color = colors[elev]
        ax.scatter(lon, lat, color=color, s=10, alpha=0.6)
    # Se podria hacer creando otra columna al dataframe que tenga el color que va a usar

    # Limito los valores de las coordenadas que se pueden ver en el mapa para que solamente muestre la zona de argentina
    ax.set_xlim(argentina.total_bounds[0], argentina.total_bounds[2])
    ax.set_ylim(argentina.total_bounds[1], argentina.total_bounds[3])

    # Configurar etiquetas y títulos
    ax.set_title('Mapa de aeropuertos segun su elevacion')
    ax.set_xlabel('Longitud')
    ax.set_ylabel('Latitud')

    # Añadir el gráfico a la aplicación de Streamlit
    st.pyplot(fig)

def airport_map_folium(dfa: pd.DataFrame):
    '''Genera un mapa de los aeropuertos de Argentina según su elevación utilizando Folium.'''
    
    def generate_map():
        '''Genera un mapa base con la librería Folium.'''
        attr = (
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
            'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
        )
        tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
        m = folium.Map(
            location=(-33.457606, -65.346857),
            control_scale=True,
            zoom_start=5,
            name='es',
            tiles=tiles,
            attr=attr
        )
        return m

    def get_color(elevation_name: str):
        '''Devuelve el color correspondiente a la elevación del aeropuerto.'''
        match elevation_name:
            case 'bajo':
                return 'green'
            case 'medio':
                return 'beige'
            case 'alto':
                return 'red'
            case 'Desconocido':
                return 'black'

    def add_marker(row: pd.Series):
        '''Añade un marcador al mapa para cada aeropuerto.'''
        color = get_color(row['elevation_name'])
        folium.Marker(
            [row['latitude_deg'], row['longitude_deg']],
            popup=row['elevation_name'],
            # Tuve que forzar ese tamaño que es el default pq no me lo tomaba bien
            icon=folium.Icon(color=color, icon= 'plane',icon_size=(41, 41))  
        ).add_to(mapa)
    
    # Crear el mapa
    mapa = generate_map()

    # Añadir los marcadores
    dfa.apply(add_marker, axis=1)

    # Integrar con Streamlit
    st.subheader('Mapa con Marcadores')
    st_folium(mapa, width=725)
# ----------------------------------- Tipos de aeropuerto -----------------------------------
def airports_types(dfa: pd.DataFrame):
    '''Genera un gráfico de torta con el porcentaje de cada tipo de aeropuerto.'''
    # Crear una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 8))

    # Filtrar datos
    dfa_filtered = dfa[dfa['type'] != 'closed']

    # Obtener los tipos y las cantidades
    types = dfa_filtered['type'].unique()
    quantity_airports = dfa_filtered['type'].value_counts()

    # Colocar los datos en columnas para mostrar en Streamlit
    coll, col2 = st.columns((2, 2))
    with coll:
        st.write(types)
    with col2:
        st.write(quantity_airports)

    # Generar el gráfico de torta
    ax.pie(quantity_airports, labels=quantity_airports.index, autopct='%1.1f%%', labeldistance=1.05, pctdistance=0.8, startangle=140)

    ax.axis('equal')  # Para que el gráfico sea un círculo

    # Añadir el gráfico a la aplicación de Streamlit
    st.pyplot(fig)
# ----------------------------------- Cantidad de aeropuertos -----------------------------------
def cant_airports(dfa: pd.DataFrame):
    '''Genera un gráfico de barras con la cantidad de aeropuertos por provincia.'''
    # Creo una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(14, 26))

    # Creo una columna con todas las provincias de argentina y reemplazo la palabra province para que solo quede el nombre
    provinces = dfa['region_name'].str.replace('Province', '').unique()

    # Creo una columna con cada provincia y su cantidad de aeropuertos respectivamente
    quantity_airports = dfa['region_name'].value_counts()

    # Creo el grafico de barras horizontal
    ax.barh(provinces, quantity_airports)
    
    # Hago que la cantidad de aetopuertos tenga un espaciado de 25
    ax.set_xticks(range(0, quantity_airports.max() + 25, 25))
    
    # Configuro los ejes y el titulo del grafico
    ax.set_xlabel('Aeropuertos')
    ax.set_ylabel('Provincias')
    ax.set_title('Gráfico de Barras de provincias segun su cantidad de aeropuertos')

    # Añado el gráfico a la aplicación de Streamlit
    st.pyplot(fig)
# --------------------------------- Mapas Lagos -------------------------------------
def lakes_map_geopandas(dfl: pd.DataFrame):
    '''Genera un mapa de los lagos de Argentina utilizando GeoPandas.'''
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

def lakes_map_folium(dfl: pd.DataFrame):
    '''Genera un mapa de los lagos de Argentina utilizando Folium.'''

    def generate_map_lake():
        '''Genera un mapa base con la librería Folium.'''
        attr = (
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
            'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
        )
        tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
        m = folium.Map(
            location=(-45.0, -65.346857),
            control_scale=True,
            zoom_start=5,
            name='es',
            tiles=tiles,
            attr=attr
        )
        return m

    def add_marker(row: pd.Series):
        '''Añade un marcador al mapa para cada lago.'''
        folium.Marker(
            [row['Latitud'], row['Longitud']],
            icon=folium.Icon(color='lightblue', icon='cloud')
        ).add_to(mapa)

    # Crear el mapa
    mapa = generate_map_lake()

    # Añadir los marcadores
    dfl.apply(add_marker, axis=1)

    # Integrar con Streamlit
    st.subheader('Mapa con Marcadores')
    st_folium(mapa, width=725)
# --------------------------------- Tamaño lagos -------------------------------------
def lake_sizes(dfl: pd.DataFrame):
    '''Genera un gráfico de barras con la cantidad de lagos por tamaño.'''
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
# ------------------------------- Grafico de Lagos -----------------------------------
def graph_lakes(dfl: pd.DataFrame):
    '''Genera un gráfico de barras con la superficie de los lagos.'''
    # Generar el gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 8))
    # Cambia 'Nombre' y 'Superficie (km²)' si es necesario
    ax.barh(dfl['Nombre'], dfl['Superficie (km²)'], color='lightgreen')  
    ax.set_title('Superficie de los Lagos')
    ax.set_xlabel('Superficie en km²')
    ax.set_ylabel('Lago')
    # Ajustar el tamaño de las etiquetas del eje y
    ax.tick_params(axis='y', labelsize=10)  
    ax.grid(True)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)