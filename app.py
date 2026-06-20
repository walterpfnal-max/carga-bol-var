import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Bolívar - RPE", page_icon="⚽")

st.title("⚽ Club Bolívar")
st.subheader("Control de Carga Interna (RPE)")

# Formulario
st.write("### 📋 Registro Diario")
jugador = st.selectbox("Selecciona el Jugador:", ["Leonel Justiniano", "Ramiro Vaca", "Bruno Sávio", "Patito Rodríguez", "Carlos Lampe"])
duracion = Skinner = st.number_input("Duración de la sesión (minutos):", min_value=1, max_value=180, value=75)
rpe = st.slider("RPE (Esfuerzo Percibido 0 al 10):", 0, 10, 5)

carga = duracion * rpe

if st.button("💾 Guardar Datos"):
    st.success(f"¡Registrado! Carga de la sesión para {jugador}: {carga} UA")
    st.balloons()

st.markdown("---")
st.write("### 📊 Datos de Control (Muestra)")
df_simulado = pd.DataFrame({
    "Jugador": ["Leonel Justiniano", "Ramiro Vaca", "Bruno Sávio"],
    "Carga (UA)": [450, 525, 375],
    "Estado (ACWR)": ["✅ Zona Dulce", "🚨 Alerta Fatiga", "✅ Zona Dulce"]
})
st.dataframe(df_simulado)
