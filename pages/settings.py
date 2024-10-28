# pages/settings.py
import streamlit as st
import json
import os

# Ruta para almacenar la configuración del usuario
CONFIG_PATH = "data/user_config.json"

# Función para cargar la configuración desde un archivo JSON
def load_config():
    # Verifica si el archivo existe, si no, devuelve configuraciones predeterminadas
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    else:
        return {"target_glucose": 100.0, "sensitivity_factor": 50.0, "carb_ratio": 10.0}  # Valores predeterminados como flotantes

# Función para guardar la configuración en un archivo JSON
def save_config(config):
    # Crear carpeta `data/` si no existe
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f)

def show_settings():
    st.title("Configuración de Insulina Personalizada")
    
    # Cargar la configuración actual del usuario
    config = load_config()

    # Entradas para los ajustes configurables, asegurando que todos los valores sean flotantes
    config["target_glucose"] = st.number_input("Objetivo de glucosa (mg/dL)", min_value=0.0, value=float(config.get("target_glucose", 100)))
    config["sensitivity_factor"] = st.number_input("Factor de sensibilidad a la insulina", min_value=1.0, value=float(config.get("sensitivity_factor", 50)))
    config["carb_ratio"] = st.number_input("Ratio insulina/carbohidratos (g/u)", min_value=0.1, value=float(config.get("carb_ratio", 10)))

    # Botón para guardar la configuración
    if st.button("Guardar Configuración"):
        save_config(config)
        st.success("Configuración guardada correctamente")
