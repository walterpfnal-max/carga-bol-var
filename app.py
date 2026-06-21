import streamlit as st
import pandas as pd
from datetime import datetime
# Importamos la conexión a Google Sheets
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Club Bolívar - RPE", page_icon="⚽", layout="centered")

# --- ESCUDO NATIVO Y CENTRADO ---
url_escudo = "https://raw.githubusercontent.com/walterpfnal-max/carga-bol-var/main/escudo.png"
col_izq, col_centro, col_der = st.columns([1, 2, 1])
with col_centro:
    st.image(url_escudo, use_container_width=True)

st.markdown("<h1 style='text-align: center;'>Club Bolívar</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #85C1E9;'>Control de Carga Interna (RPE)</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- CONEXIÓN A GOOGLE SHEETS ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    # Leemos los datos existentes
    df_existente = conn.read(ttl=0)
except Exception as e:
    df_existente = pd.DataFrame(columns=["Fecha", "Jugador", "Duracion", "RPE", "Carga"])

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

if st.button("💾 Guardar Datos"):
    # Creamos la nueva fila con los datos ingresados
    nueva_fila = pd.DataFrame([{
        "Fecha": fecha_hoy,
        "Jugador": jugador,
        "Duracion": duracion,
        "RPE": rpe,
        "Carga": carga
    }])
    
    # Combinamos los datos viejos con los nuevos
    df_actualizado = pd.concat([df_existente, nueva_fila], ignore_index=True)
    
    # Mandamos todo de vuelta a tu Google Sheets
    conn.update(data=df_actualizado)
    
    st.success(f"¡Registrado con éxito! Carga de la sesión para {jugador}: {carga} UA")
    st.balloons()

st.markdown("---")
st.write("### 📊 Historial de Cargas Registradas")
# Mostramos la tabla real de lo que se va guardando en tu Google Sheets
st.dataframe(df_existente)
