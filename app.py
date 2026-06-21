import streamlit as st
import pandas as pd

st.set_page_config(page_title="Club Bolívar - RPE", page_icon="⚽", layout="centered")

# --- ESCUDO NATIVO Y CENTRADO ---
# Se conecta de manera directa con el archivo que subiste a tu propio repositorio
url_escudo = "https://raw.githubusercontent.com/walterpfnal-max/carga-bol-var/main/escudo.png"

# Estructura de columnas para centrar y dar espacio al escudo en grande
col_izq, col_centro, col_der = st.columns([1, 2, 1])
with col_centro:
    st.image(url_escudo, use_container_width=True)

# Títulos del Club Centrados
st.markdown("<h1 style='text-align: center;'>Club Bolívar</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #85C1E9;'>Control de Carga Interna (RPE)</h3>", unsafe_allow_html=True)

st.markdown("---")

# --- REGISTRO DIARIO ---
st.write("### 📋 Registro Diario de Sesión")

plantel_bolivar = [
    "Carlos Lampe",
    "Diego Mendez",
    "Leonel Justiniano", 
    "Juan Jose Lopez", 
    "Santiago Echeverria", 
    "Patito Rodríguez",
    "Jesús Sagredo",
    "José Sagredo",
    "Xavier Arreaga",
    "Luis Paz",
    "Escleizon Freita",
    "Ervin Vaca",
    "Carlos amelgar",
    "Lucas Chávez",
    "Robson Matheus",
    "Ervin Saavedra",
    "Martin Cauteruccio",
    "Dorni Romero",
    "Jhon Garcia",
    "Carlos Sejas",
    "Anderson Ayhuana",
    "Jhon Velasquez",
    "Cristian Lopez",
    "Jesus Velasquez",
    "Heiden Butron",
    "Matias Galindo",
]

jugador = st.selectbox("Selecciona el Jugador:", sorted(plantel_bolivar))
duracion = st.number_input("Duración de la sesión (minutos):", min_value=1, max_value=180, value=75, step=5)
rpe = st.slider("RPE (Esfuerzo Percibido 0 al 10):", 0, 10, 5)

carga = duracion * rpe

if st.button("💾 Guardar Datos"):
    st.success(f"¡Registrado con éxito! Carga de la sesión para {jugador}: {carga} UA")
    st.balloons()

st.markdown("---")
st.write("### 📊 Datos de Control (Muestra)")
df_simulado = pd.DataFrame({
    "Jugador": ["Leonel Justiniano", "Ramiro Vaca", "Bruno Sávio"],
    "Carga (UA)": [450, 525, 375],
    "Estado (ACWR)": ["✅ Zona Dulce", "🚨 Alerta Fatiga", "✅ Zona Dulce"]
})
st.dataframe(df_simulado)
