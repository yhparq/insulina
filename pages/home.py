# pages/home.py
import streamlit as st

def show_home():
    st.title("Bienvenido al Asistente de Dosis de Insulina")
    # st.image("assets/logo.png", use_column_width=True)  # Añadir logo si lo tienes
    st.markdown("""
    ### Esta aplicación te ayudará a calcular las dosis de insulina adecuadas basadas en tus niveles de glucosa y la ingesta de carbohidratos.
    """)
    st.markdown("""
    ### Características:
    - Calculadora de dosis de insulina basada en tus datos personales.
    - Registro de tus niveles de glucosa y consumo de carbohidratos.
    - Historial de dosis y reportes personalizados.
    - Configuración personalizada de ratios y sensibilidad de insulina.
    - Recordatorios y notificaciones.
    """)

    st.info("Utiliza la barra de navegación a la izquierda para acceder a las funciones de la aplicación.")
