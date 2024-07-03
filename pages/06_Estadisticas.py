from resources import stats
import streamlit as st  
import json
import pandas as pd
import pathlib

# Ruta del archivo JSON
route = pathlib.Path("./data_users/results.json")

# Data variable global
with open(route, 'r') as f:
    data = json.load(f)

# Si el archivo no está vacío se ejecutan las estadísticas.
if data != []:  
    # Elimina warning
    st.set_option('deprecation.showPyplotGlobalUse', False)


    df = pd.DataFrame(data)

    # ------------------------------------------------------------

    stats.user_gender(df) # PUNTO 1

    st.divider()

    stats.percentage_above_average_score(df) # PUNTO 2

    st.divider()

    stats.matchs_per_day(df) # PUNTO 3

    st.divider()

    stats.average_correct_answers_per_month(df) # PUNTO 4

    st.divider()

    stats.top10_users_between(df) # PUNTO 5

    st.divider()

    stats.hardest_datasets(df) # PUNTO 6

    st.divider()

    stats.points_in_time(df) # PUNTO 7

    st.divider()

    stats.best_theme_by_gender(df) # PUNTO 8

    st.divider()

    stats.average_difficulty(df) # PUNTO 9

    st.divider()

    stats.user_streak(df) # PUNTO 10
else:
    st.title("No hay datos para mostrar ya que no se ha jugado ninguna partida.")