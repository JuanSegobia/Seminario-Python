import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from resources import widgets as w

# Cargar los datos desde un archivo CSV
dfa = pd.read_csv('./custom_datasets/processed_airports.csv')
dfl = pd.read_csv('./custom_datasets/lagos_arg.csv')

st.markdown('<a name="titulo"></a>', unsafe_allow_html=True)
st.title('Datos Interesantes')

st.markdown('''
    - [Ubicaciones de los aeropuertos segun su elevacion:](#mapas-aeropuertos)
    - [Porcentajes de tipos de aeropuertos](#porcentaje-tipo-aeropuerto)
    - [Cantidad de aeropuertos por provincia](#ranking-provincias)
    - [Ubicaciones de los lagos](#ubicaciones-de-lagos)
    - [Superficie por km² de cada lago](#supericie-km-cuadrados)
    - [Grafico de barras por tamaño de lagos](#tamaño-de-lagos)
''')

st.divider()

# ----------------------- AEROPUERTOS -----------------------

st.markdown('<a name="mapas-aeropuertos"></a>', unsafe_allow_html=True)
st.header('Mapa de aeropuertos segun su elevacion:')
st.write('🟢 Elevacion Baja')
st.write('🟡 Elevacion Media')
st.write('🔴 Elevacion Alta')
st.write('⚫ Elevacion Desconocida')

airport_maps = st.tabs(["Geopandas", "Folium"])

with airport_maps[0]:
    w.airport_map_geopandas(dfa)

with airport_maps[1]:
    w.airport_map_folium(dfa)

st.markdown('- [Volver al menu](#titulo)')
st.markdown('- [Siguiente](#porcentaje-tipo-aeropuerto)')
st.divider()

# ----------------------- Widget A1 -----------------------

st.markdown('<a name="porcentaje-tipo-aeropuerto"></a>', unsafe_allow_html=True)
st.header('Gráfico de torta con porcentaje de cada tipo de aeropuerto')

w.airports_types(dfa)

st.markdown('- [Volver al menu](#titulo)')
st.markdown('- [Siguiente](#ranking-provincias)')
st.divider()

# ----------------------- Widget A2 -----------------------

st.markdown('<a name="ranking-provincias"></a>', unsafe_allow_html=True)
st.header('Mapa de provincias segun su cantidad de aeropuertos')

w.cant_airports(dfa)

st.markdown('- [Volver al menu](#titulo)')
st.markdown('- [Siguiente](#ubicaciones-de-lagos)')
st.divider()

# ----------------------- LAGOS -----------------------

st.markdown('<a name="ubicaciones-de-lagos"></a>', unsafe_allow_html=True)
st.header('Mapa de ubicación de lagos en Argentina:')

lakes_maps = st.tabs(["Folium", "Geopandas"])

with lakes_maps[0]:
    w.lakes_map_folium(dfl)

with lakes_maps[1]:
    w.lakes_map_geopandas(dfl)

st.markdown('- [Volver al menu](#titulo)')
st.markdown('- [Siguiente](#supericie-km-cuadrados)')
st.divider()

# ----------------------- Widget L1 -----------------------

st.markdown('<a name="supericie-km-cuadrados"></a>', unsafe_allow_html=True)
st.header('Mapa de superficie por km² de cada Lago')

w.graph_lakes(dfl)

st.markdown('- [Volver al menu](#titulo)')
st.markdown('- [Siguiente](#tamaño-de-lagos)')
st.divider()

# ----------------------- Widget L2 -----------------------

st.markdown('<a name="tamaño-de-lagos"></a>', unsafe_allow_html=True)
st.header('Grafico de barras de los tamaños de los lagos:')

w.lake_sizes(dfl)

st.markdown('- [Volver al menu](#titulo)')
st.divider()
