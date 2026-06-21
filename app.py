import streamlit as st
import json
import requests
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Club Bolívar - RPE", page_icon="⚽", layout="centered")

# URL de tu Google Apps Script (Debe quedar exactamente así)
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycybyh7V7fAAn17L_ACuQ04Cg_Z-1kWIH8T1AaELuvAZ-LR8BGPH8_L2Kp51_NmT7B8lR5tQ/exec"

# Encabezado de la App
st.markdown("<h1 style='text-align: center;'>🔵 Club Bolívar 🔵</h1>", unsafe_url_allowed=True)
st.markdown("<h3 style='text-align: center;'>Control de Carga Interna (RPE)</h3>", unsafe_url_allowed=True)

st.markdown("---")

st.subheader("📋 Registro Diario de Sesión")

# Formulario de entrada
jugadores = ["Bruno Sávio", "Carlos Lampe", "Ervin Vaca", "Patito Rodríguez", "Jesús Sagredo"]
jugador = st.selectbox("Selecciona el Jugador:", jugadores)

duracion = st.number_input("Duración de la sesión (minutos):", min_value=1, max_value=240, value=60, step=5)
rpe = st.slider("RPE (Esfuerzo Percibido 0 al 10):", min_value=0, max_value=10, value=5)

# Cálculo automático de la carga
carga = duracion * rpe
st.metric(label="Carga Calculada (UA)", value=f"{carga} UA")

fecha_hoy = datetime.now().strftime("%Y-%m-%d")

# Botón para enviar datos
if st.button("💾 Guardar Datos"):
    datos_sesion = {
        "Fecha": fecha_hoy,
        "Jugador": jugador,
        "Duracion": int(duracion),
        "RPE": int(rpe),
        "Carga": int(carga)
    }
    
    try:
        # Enviamos los datos al puente de Google Apps Script
        response = requests.post(WEBHOOK_URL, data=json.dumps(datos_sesion))
        
        if response.status_code == 200:
            st.success(f"¡Registrado con éxito! Carga para {jugador}: {carga} UA")
            st.balloons()
        else:
            st.error(f"Error del servidor de Google (Código {response.status_code})")
            
    except Exception as e:
        st.error(f"Error de conexión: {e}")
