import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Club Bolívar - RPE", page_icon="⚽", layout="centered")

# --- ESCUDO Y TÍTULO ---
# Usamos el enlace directo del escudo oficial del Club Bolívar en alta definición
url_escudo = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Club_Bol%C3%ADvar_Logo.png"

col1, col2 = st.columns([1, 4])
with col1:
    st.image(url_escudo, width=90)
with col2:
    st.title("Club Bolívar")
    st.subheader("Control de Carga Interna (RPE)")

st.markdown("---")

# --- REGISTRO DIARIO ---
st.write("### 📋 Registro Diario de Sesión")

# 👇 ¡AQUÍ MODIFICAS TU LISTA DE JUGADORES! 
# Solo cambia los nombres entre comillas o añade más separados por comas.
plantel_bolivar = [
    "Carlos Lampe", 
    "Leonel Justiniano", 
    "Ramiro Vaca", 
    "Bruno Sávio", 
    "Patito Rodríguez",
    "Jesús Sagredo",
    "José Sagredo",
    "Carmelo Algarañaz",
    "Fernando Saucedo"
]

jugador = st.selectbox("Selecciona el Jugador:", plantel_bolivar)
duracion = st.number_input("Duración de la sesión (minutos):", min_value=1, max_value=180, value=75, step=5)
rpe = st.slider("RPE (Esfuerzo Percibido 0 al 10):", 0, 10, 5)

# Cálculo automático de Unidades Arbitrarias
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

  
