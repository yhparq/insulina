# pages/history.py
import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Ruta para almacenar el historial del usuario
DATA_PATH = "data/user_data.csv"

# Cargar el historial desde el archivo CSV o crear un archivo vacío con las columnas necesarias
def load_history():
    if not os.path.exists(DATA_PATH) or os.path.getsize(DATA_PATH) == 0:
        # Crear un DataFrame vacío con las columnas correctas
        history = pd.DataFrame(columns=["Día", "Mes", "Año", "Glucosa (mg/dL)", "Carbohidratos (g)", "Dosis Insulina (u)"])
        history.to_csv(DATA_PATH, index=False)
    else:
        history = pd.read_csv(DATA_PATH)
    return history

# Guardar una nueva entrada en el historial
def save_history(glucose, carbs, dose):
    history = load_history()
    current_date = datetime.now()
    new_entry = pd.DataFrame({
        "Día": [current_date.day],
        "Mes": [current_date.month],
        "Año": [current_date.year],
        "Glucosa (mg/dL)": [glucose],
        "Carbohidratos (g)": [carbs],
        "Dosis Insulina (u)": [dose]
    })
    history = pd.concat([history, new_entry], ignore_index=True)
    history.to_csv(DATA_PATH, index=False)

def show_history():
    st.title("Historial de Dosis de Insulina")
    
    # Mostrar el historial de datos
    history = load_history()
    
    if not history.empty:
        st.dataframe(history)
    else:
        st.info("No se ha registrado ningún dato aún.")
