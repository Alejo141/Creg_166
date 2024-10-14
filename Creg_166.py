import streamlit as st
import pandas as pd

# Instalación de openpyxl para leer archivos Excel
import pip
pip.main(["install", "openpyxl"])

# Limpiar caché de datos
st.cache_data.clear()

# Título de la aplicación
st.title("Cálculos CREG 166")

# Subtítulo para Inversión Pública
st.subheader("Inversión Pública")

# Crear columnas para los elementos de inversión
col1, col2, col3, col4 = st.columns(4)

# Diccionario para almacenar los valores de inversión
inversiones = {
    "Modulo, Estructura, OE y OC": {"valor": 83151, "si": 0},
    "Controlador": {"valor": 15986, "si": 0},
    "Inversor": {"valor": 25617, "si": 0},
    "Batería": {"valor": 104539, "si": 0}
}

# Generar radio buttons dinámicamente
for idx, (nombre, datos) in enumerate(inversiones.items()):
    with [col1, col2, col3, col4][idx]:
        seleccion = st.radio(nombre, ['Si', 'No'])
        inversiones[nombre]['seleccionado'] = datos['si'] if seleccion == 'Si' else datos['valor']

# Cálculo de Gi0
Gi0 = sum([datos['seleccionado'] for datos in inversiones.values()])
Gaom0 = 86525
C0 = 23181
IPP0 = 122.59
IPC0 = 104.97

# Mostrar resultados intermedios
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.caption("Gi0:")
    st.code(Gi0)
with col2:
    st.caption("Gaom0:")
    st.code(Gaom0)
with col3:
    st.caption("C0:")
    st.code(C0)
with col4:
    st.caption("IPP0:")
    st.code(IPP0)
with col5:
    st.caption("IPC0:")
    st.code(IPC0)

# Cálculo de G0
G0 = Gi0 + Gaom0
st.caption("G0:")
st.code(G0)

# Selección de periodo
st.subheader("Selección del periodo m-1 para realizar el cálculo:")

col1, col2 = st.columns(2)
with col1:
    año = st.selectbox('Seleccione el año', [2020, 2021, 2022, 2023])
with col2:
    mes = st.selectbox('Seleccione el periodo', ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])

# Construcción del periodo en formato mes-año
año_mes = f"{mes} {año}"
st.caption(año_mes)

# Simplificación de la lógica del cálculo de mes siguiente
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
indice_mes = meses.index(mes)
if indice_mes == 11:  # Si es diciembre, avanzar al siguiente año
    mes_siguiente = meses[0]
    año_siguiente = año + 1
else:
    mes_siguiente = meses[indice_mes + 1]
    año_siguiente = año

# Mostrar resultado del siguiente periodo
st.subheader(f"El cálculo corresponde a {mes_siguiente} {año_siguiente}")

# Cargar y mostrar tablas IPP e IPC
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tabla IPP")
    ipp = pd.read_excel("IPP.xlsx", sheet_name="2.1")
    ipp = ipp.rename(columns=lambda x: x.replace('pr)*', '').strip())
    
    if st.button('Mostrar Tabla IPP'):
        st.write(ipp)

    # Obtener IPPm_1 para el cálculo
    IPPm_1 = ipp[año_mes].iloc[0]
    st.caption("IPPm_1:")
    st.code(IPPm_1)

with col2:
    st.subheader("Tabla IPC")
    ipc = pd.read_excel("IPC.xlsx").set_index("Año(aaaa)-Mes(mm)")
    
    if st.button('Mostrar Tabla IPC'):
        st.write(ipc)
    
    IPCm_1 = ipc.loc[año_mes, 'Índice']
    st.caption("IPCm_1:")
    st.code(IPCm_1)

# Cálculo de Gm y Cm
col1, col2 = st.columns(2)

with col1:
    Gm = G0 * (IPPm_1 / IPP0)
    st.caption("Gm:")
    st.code(Gm)

with col2:
    Cm = C0 * (IPCm_1 / IPC0)
    st.caption("Cm:")
    st.code(Cm)

# Cálculo final de CU
CU = Gm + Cm
st.subheader("CU:")
st.code(CU)