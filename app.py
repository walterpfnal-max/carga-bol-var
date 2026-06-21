import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime

st.set_page_config(page_title="Club Bolívar - RPE", page_icon="⚽", layout="centered")

# --- ESCUDO NATIVO Y CENTRADO ---
url_escudo = "https://raw.githubusercontent.com/walterpfnal-max/carga-bol-var/main/escudo.png"
col_izq, col_centro, col_der = st.columns([1, 2, 1])
with col_centro:
    st.image(url_escudo, use_container_width=True)

st.markdown("<h1 style='text-align: center;'>Club Bolívar</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #85C1E9;'>Control de Carga Interna (RPE)</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- REGISTRO DIARIO ---
st.write("### 📋 Registro Diario de Sesión")

plantel_bolivar = [
    "Carlos Lampe", "Rubén Cordano", "Leonel Justiniano", "Ramiro Vaca", 
    "Bruno Sávio", "Patito Rodríguez", "Jesús Sagredo", "José Sagredo", 
    "Yomar Rocha", "Luis Paz", "Fernando Saucedo", "Ervin Vaca", 
    "Carmelo Algarañaz", "Lucas Chávez"
]

jugador = st.selectbox("Selecciona el Jugador:", sorted(plantel_bolivar))
duracion = st.number_input("Duración de la sesión (minutos):", min_value=1, max_value=180, value=75, step=5)
rpe = st.slider("RPE (Esfuerzo Percibido 0 al 10):", 0, 10, 5)

carga = duracion * rpe
fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M")

# 🔗 AQUÍ PEGA TU ENLACE DE GOOGLE APPS SCRIPT
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbyh7V7fAAni7L_ACuQ04Cg_Z-lkWIH8TiAAeLuvAZ-LR8BGPH8_L2Kp5i_Nm7T88lR5tQ/exec

if st.button("💾 Guardar Datos"):
    if WEBHOOK_URL == "https://script.google.com/macros/s/AKfycbyh7V7fAAni7L_ACuQ04Cg_Z-lkWIH8TiAAeLuvAZ-LR8BGPH8_L2Kp5i_Nm7T88lR5tQ/exec")
    else:
        datos_sesion = {
            "Fecha": fecha_hoy,
            "Jugador": jugador,
            "Duracion": int(duracion),
            "RPE": int(rpe),
            "Carga": int(carga)
        }
        
        try:
            response = requests.post(WEBHOOK_URL, data=json.dumps(datos_sesion))
            if response.status_code == 200:
                st.success(f"¡Registrado con éxito! Carga para {jugador}: {carga} UA")
                st.balloons()
            else:
                st.error("Error al conectar con la base de datos.")
        except Exception as e:
            st.error(f"Error de conexión: {e}")
