import streamlit as st
import pandas as pd

st.set_page_config(page_title="HAND - Plan de Negocios", layout="wide")

st.title("Etapa 1: Prueba de Concepto")

# Horarios
st.header("Configuración de Operación")
days_open = st.multiselect("Días de apertura", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], default=["Jueves", "Viernes", "Sábado", "Domingo"])
start_hour = st.time_input("Hora de apertura", value=pd.to_datetime("17:00").time())
end_hour = st.time_input("Hora de cierre", value=pd.to_datetime("23:00").time())

# Escenarios
st.header("Escenarios de Ventas")
scenario = st.selectbox("Escenario", ["Conservador", "Esperado", "Óptimo"])
orders_per_day = st.slider("Órdenes por día", min_value=10, max_value=100, value=30 if scenario=="Esperado" else 20 if scenario=="Conservador" else 50)
burgers_per_order = st.number_input("Burgers por orden (promedio)", value=2.1)
ticket_avg = st.number_input("Ticket promedio ($)", value=14.0)

# Empleados
st.header("Configuración de Personal")
col1, col2, col3 = st.columns(3)
with col1:
    mgr_salary = st.number_input("Salario semanal - Gerente", value=600)
with col2:
    cook_salary = st.number_input("Salario semanal - Cocinero", value=500)
with col3:
    asst_salary = st.number_input("Salario semanal - Asistente", value=400)

# Alquiler
st.header("Alquiler")
rent = st.selectbox("Costo mensual de alquiler", [3000, 4000, 4500])
weekly_rent = rent / 4

# Cálculos
days_count = len(days_open)
weekly_orders = orders_per_day * days_count
total_burgers = weekly_orders * burgers_per_order
food_cost = st.number_input("Costo unitario promedio por burger", value=4.5)
weekly_cost = total_burgers * food_cost
weekly_income = weekly_orders * ticket_avg
weekly_salaries = mgr_salary + cook_salary + asst_salary
weekly_net = weekly_income - (weekly_cost + weekly_salaries + weekly_rent)

# Resultados
st.header("Resultados Semanales")
st.metric("Ingresos", f"${weekly_income:,.2f}")
st.metric("Costo insumos", f"${weekly_cost:,.2f}")
st.metric("Sueldos", f"${weekly_salaries:,.2f}")
st.metric("Alquiler semanal", f"${weekly_rent:,.2f}")
st.metric("Utilidad neta", f"${weekly_net:,.2f}")
