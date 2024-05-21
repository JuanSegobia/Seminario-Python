import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from resources import widgets as w

# Cargar los datos desde un archivo CSV
dfa = pd.read_csv('./custom_datasets/processed_airports.csv')

dfl = pd.read_csv('./custom_datasets/lagos_arg.csv')

w.airport_map(dfa)

st.divider()

w.airports_types(dfa)

st.divider()

w.cant_airports(dfa)

st.divider()

w.lakes_map(dfl)

st.divider()

w.graph_lakes(dfl)

st.divider()

w.lake_sizes(dfl)

st.divider()
