# pages/calculator.py
import streamlit as st
from utils.calculations import calculate_insulin_dose
from pages.history import save_history  # Importar la función para guardar el historial
import json
import os

# Ruta para cargar la configuración del usuario
CONFIG_PATH = "data/user_config.json"

# Función para cargar la configuración desde un archivo JSON
def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    else:
        return {"target_glucose": 100.0, "sensitivity_factor": 50.0, "carb_ratio": 10.0}  # Valores predeterminados

def show_calculator():
    st.title("Calculadora de Dosis de Insulina")
    
    # Cargar configuración del usuario
    config = load_config()

    # Entrada de datos del usuario, utilizando valores predeterminados desde la configuración
    glucose_level = st.number_input("Nivel de glucosa actual (mg/dL)", min_value=0.0)
    carb_intake = st.number_input("Ingesta de carbohidratos (g)", min_value=0.0)
    target_glucose = st.number_input("Objetivo de glucosa (mg/dL)", min_value=0.0, value=float(config["target_glucose"]))
    sensitivity_factor = st.number_input("Factor de sensibilidad a la insulina", min_value=1.0, value=float(config["sensitivity_factor"]))
    carb_ratio = st.number_input("Ratio insulina/carbohidratos (g/u)", min_value=0.1, value=float(config["carb_ratio"]))

    if st.button("Calcular Dosis de Insulina"):
        dose = calculate_insulin_dose(glucose_level, carb_intake, target_glucose, sensitivity_factor, carb_ratio)
        
        # Guardar automáticamente en el historial
        save_history(glucose_level, carb_intake, dose)
        
        st.success(f"Dosis recomendada de insulina: {dose:.2f} unidades")
        st.info("La dosis ha sido guardada automáticamente en el historial.")
