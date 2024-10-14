import streamlit as st
import pandas as pd

import pip
pip.main(["install", "openpyxl"])

######### Título Pag ###########
st.title("Cálculos CREG 166")

######### Constantes ###########

st.subheader("Inversión Pública?")

#Crear dos columnas con el mismo tamaño
col1, col2, col3, col4 = st.columns(4)

with col1:   
    Modulo = st.radio('Modulo, Estructura, OE y OC', ['Si', 'No'])
    if Modulo == 'Si':
        Mod = 0
    else:
        Mod = 83151
    
with col2:
    Controlador = st.radio('Controlador', ['Si', 'No'])
    if Controlador == 'Si':
        Con = 0
    else:
        Con = 15986

with col3:
    Inversor = st.radio('Inversor', ['Si', 'No'])
    if Inversor == 'Si':
        Inv = 0
    else:
        Inv = 25617
with col4:
    Bateria = st.radio('Batería', ['Si', 'No'])
    if Bateria == 'Si':
        Bat = 0
    else:
        Bat = 104539

#Crear dos columnas con el mismo tamaño
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Gi0 = Mod + Con + Inv + Bat
    st.caption("Gi0:")
    st.code(Gi0)

with col2:
    Gaom0 = 86525
    st.caption("Gaom0:")
    st.code(Gaom0)

with col3:
    C0 = 23181
    st.caption("C0:")
    st.code(C0)

with col4:
    IPP0 = 122.59
    st.caption("IPP0:")
    st.code(IPP0)

with col5:
    IPC0 = 104.97
    st.caption("IPC0:")
    st.code(IPC0)

######### Cálculo G0 ###########
G0 = Gi0 + Gaom0
st.caption("G0:")
st.code(G0)


######################## Selección del mes al cual se le realizará el cálculo #############################
st.subheader("Selección del periodo al cual se le realizará el cálculo")

#Crear dos columnas con el mismo tamaño
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    año = st.selectbox('Seleccione el año', [2020, 2021, 2022, 2023])

with col2:
    mes = st.selectbox('Seleccione el periodo', ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])


año_mes = f"{mes}{año}"

######### Cargar excel IPP (Se deberá actualizar todos los meses ###########
ipp = pd.read_excel("IPP.xlsx", sheet_name = "2.1")
# Cambiar solo el nombre de algunas columnas
ipp = ipp.rename(columns={'ene-21 (pr)*': 'Enero 2021', 'feb-21 (pr)*': 'Febrero 2021'})
st.write(ipp)

#st.code(ipp["May-23 (pr)*"])

IPPm_1 = ipp[año_mes][0]

#IPPm_1 = ipp["May-23 (pr)*"][0] #Se trae el IPP del mes que se quiere calcular

st.caption("IPPm_1:")
st.code(IPPm_1)

######### Cálculo Gm ###########
Gm = G0 * (IPPm_1/IPP0)
st.caption("Gm:")
st.code(Gm)


######### Cargar Excel IPC (Se deberá actualizar todos los meses) ###########
df = pd.read_excel("IPC.xlsx")
#st.write(df)

ipc = df.set_index("Año(aaaa)-Mes(mm)")
st.write(ipc)

IPCm_1 = ipc["Índice"][202307] #Se trae el IPC del mes que se quiere calcular

st.caption("IPCm_1:")
st.code(IPCm_1)

######### Cálculo Cm ###########
Cm = C0 * (IPCm_1/IPC0)
st.caption("Cm:")
st.code(Cm)


######### Cálculo CU ###########
CU = Gm + Cm
st.subheader("CU:")
st.code(CU)