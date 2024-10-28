# pages/graphs.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta para almacenar el historial del usuario
DATA_PATH = "data/user_data.csv"

# Cargar el historial desde el archivo CSV o crear un archivo vacío si no existe
def load_history():
    if os.path.exists(DATA_PATH) and os.path.getsize(DATA_PATH) > 0:
        history = pd.read_csv(DATA_PATH)
        
        # Verificar si las columnas necesarias están presentes y convertirlas a enteros
        if set(["Día", "Mes", "Año"]).issubset(history.columns):
            history["Día"] = history["Día"].astype(int)
            history["Mes"] = history["Mes"].astype(int)
            history["Año"] = history["Año"].astype(int)
            
            # Convertir día, mes y año en una columna de fecha
            history["Fecha"] = pd.to_datetime(history[["Año", "Mes", "Día"]])
            return history
        else:
            st.warning("El archivo de historial no contiene las columnas necesarias: 'Día', 'Mes', y 'Año'.")
            return pd.DataFrame()
    else:
        st.warning("No hay datos en el historial para mostrar gráficos.")
        return pd.DataFrame()

def show_graphs():
    st.title("Gráficos de Historial de Insulina")
    
    # Cargar el historial de datos
    history = load_history()
    
    if not history.empty:
        # Gráfico de Línea: Tendencia de los Niveles de Glucosa
        st.subheader("Tendencia de Niveles de Glucosa")
        plt.figure(figsize=(10, 5))
        plt.plot(history["Fecha"], history["Glucosa (mg/dL)"], marker="o", color="blue")
        plt.xlabel("Fecha")
        plt.ylabel("Glucosa (mg/dL)")
        plt.title("Tendencia de Niveles de Glucosa")
        plt.xticks(rotation=45)
        st.pyplot(plt)
        plt.clf()

        # Gráfico de Barras: Carbohidratos vs Dosis de Insulina
        st.subheader("Ingesta de Carbohidratos vs Dosis de Insulina")
        plt.figure(figsize=(10, 5))
        width = 0.4
        plt.bar(history["Fecha"] - pd.Timedelta(days=0.2), history["Carbohidratos (g)"], width=width, label="Carbohidratos (g)", color="orange")
        plt.bar(history["Fecha"] + pd.Timedelta(days=0.2), history["Dosis Insulina (u)"], width=width, label="Dosis Insulina (u)", color="green")
        plt.xlabel("Fecha")
        plt.ylabel("Cantidad")
        plt.title("Carbohidratos vs Dosis de Insulina")
        plt.legend()
        plt.xticks(rotation=45)
        st.pyplot(plt)
        plt.clf()

        # Histograma: Distribución de Dosis de Insulina
        st.subheader("Distribución de Dosis de Insulina")
        plt.figure(figsize=(10, 5))
        plt.hist(history["Dosis Insulina (u)"], bins=10, color="purple", edgecolor="black")
        plt.xlabel("Dosis Insulina (u)")
        plt.ylabel("Frecuencia")
        plt.title("Distribución de Dosis de Insulina")
        st.pyplot(plt)
    else:
        st.info("Aún no hay datos en el historial para mostrar gráficos.")
