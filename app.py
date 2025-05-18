import streamlit as st
import joblib
import pandas as pd

# ✅ Rerun seguro para versiones nuevas de Streamlit
try:
    from streamlit.runtime.scriptrunner import rerun
except ImportError:
    rerun = lambda: st.warning("⚠️ Reinicio no disponible en esta versión de Streamlit.")

# ✅ Verificar si se debe reiniciar
if st.session_state.get("reset_now", False):
    st.session_state.clear()
    rerun()

# Cargar el modelo
modelo = joblib.load("modelo_churn_xgb.pkl")

# Configurar página
st.set_page_config(page_title="Predicción de Churn", page_icon="📊")
st.title("📊 Predicción de Churn de Clientes")
st.markdown("""
Esta herramienta predice si un cliente de telecomunicaciones tiene probabilidad de **abandonar el servicio** (churn).

🔎 Basado en características como el tiempo como cliente, el tipo de contrato y los servicios contratados, podés anticipar qué clientes están en riesgo.

👉 Completá los datos del cliente y hacé clic en **Predecir**.
""")

# Valores por defecto
defaults = {
    'total_charges': 0.0,
    'monthly_charges': 0.0,
    'tenure': 0,
    'gender': "Female",
    'partner': "No",
    'online_security': "No",
    'paperless': "No",
    'contract_two_year': "No",
    'fiber_optic': "No",
    'electronic_check': "No"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Inputs
total_charges = st.number_input("Total Charges ($)", min_value=0.0, step=10.0, key='total_charges')
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, step=1.0, key='monthly_charges')
tenure = st.slider("Meses de permanencia (Tenure)", min_value=0, max_value=72, key='tenure')

gender = st.selectbox("Género", ["Female", "Male"], key='gender')
partner = st.selectbox("¿Tiene pareja?", ["No", "Sí"], key='partner') == "Sí"
online_security = st.selectbox("¿Tiene seguridad en línea?", ["No", "Sí"], key='online_security') == "Sí"
paperless = st.selectbox("¿Usa facturación sin papel?", ["No", "Sí"], key='paperless') == "Sí"
contract_two_year = st.selectbox("¿Tiene contrato por 2 años?", ["No", "Sí"], key='contract_two_year') == "Sí"
fiber_optic = st.selectbox("¿Tiene fibra óptica?", ["No", "Sí"], key='fiber_optic') == "Sí"
electronic_check = st.selectbox("¿Paga con cheque electrónico?", ["No", "Sí"], key='electronic_check') == "Sí"

# Crear DataFrame
input_df = pd.DataFrame([{
    'TotalCharges': total_charges,
    'MonthlyCharges': monthly_charges,
    'tenure': tenure,
    'InternetService_Fiber optic': int(fiber_optic),
    'PaymentMethod_Electronic check': int(electronic_check),
    'Contract_Two year': int(contract_two_year),
    'PaperlessBilling': int(paperless),
    'gender': 1 if gender == "Female" else 0,
    'OnlineSecurity': int(online_security),
    'Partner': int(partner)
}])

# Botón de predicción
if st.button("🔮 Predecir Churn", key="predict"):
    pred = modelo.predict(input_df)[0]
    proba = modelo.predict_proba(input_df)[0][1]

    if pred == 1:
        st.error(f"⚠️ El cliente tiene ALTA probabilidad de irse. (Probabilidad: {proba:.2%})")
    else:
        st.success(f"✅ El cliente probablemente permanecerá. (Probabilidad de churn: {proba:.2%})")

    # Explicación
    st.markdown("### 🧠 ¿Por qué esta predicción?")

    st.markdown("#### ✅ Factores que ayudan a retener al cliente:")
    if tenure >= 12:
        st.markdown("- **Buena antigüedad**: clientes con más meses suelen ser más leales.")
    if contract_two_year:
        st.markdown("- **Contrato por 2 años**: fuerte indicador de permanencia.")
    if online_security:
        st.markdown("- **Cuenta con seguridad en línea**, lo que indica mayor compromiso.")
    if not electronic_check:
        st.markdown("- No usa cheque electrónico, lo cual se asocia a menor riesgo.")
    if partner:
        st.markdown("- Tiene pareja, lo cual históricamente reduce ligeramente el churn.")

    st.markdown("#### ⚠️ Factores de riesgo a considerar:")
    if tenure <= 6:
        st.markdown("- **Poca permanencia**: los clientes nuevos tienden a irse más fácilmente.")
    if not contract_two_year:
        st.markdown("- **No tiene contrato largo**, lo cual permite desvinculación fácil.")
    if not online_security:
        st.markdown("- **No tiene seguridad en línea**, puede ser un cliente menos vinculado.")
    if electronic_check:
        st.markdown("- **Paga con cheque electrónico**, uno de los métodos con mayor tasa de churn.")
    if paperless:
        st.markdown("- Aunque usa facturación digital, no siempre es un indicador de retención.")

# 🔁 Botón para reiniciar
if st.button("🔁 Reiniciar formulario", key="reset_button"):
    st.session_state["reset_now"] = True
    rerun()
