# app.py
import streamlit as st
from pages import home, history, settings, calculator, graphs  # Importar graphs

# Configuración general de la app
st.set_page_config(
    page_title="Asistente de Dosis de Insulina",
    page_icon="💉",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Barra lateral de navegación
st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a", ["Inicio", "Historial", "Configuración", "Calculadora", "Gráficos"])

# Mostrar la página correspondiente
if page == "Inicio":
    home.show_home()
elif page == "Historial":
    history.show_history()
elif page == "Configuración":
    settings.show_settings()
elif page == "Calculadora":
    calculator.show_calculator()
elif page == "Gráficos":
    graphs.show_graphs()
