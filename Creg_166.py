import streamlit as st
import pandas as pd

import pip
pip.main(["install", "openpyxl"])

st.cache_data.clear()

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
st.subheader("Selección el periodo m-1 para realizar el cálculo:")

#Crear dos columnas con el mismo tamaño
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    año = st.selectbox('Seleccione el año', [2020, 2021, 2022, 2023])

with col2:
    mes = st.selectbox('Seleccione el periodo', ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])


año_mes = f"{mes}{" "}{año}"
st.caption(año_mes)

######### Cargar excel IPP (Se deberá actualizar todos los meses ###########
ipp = pd.read_excel("IPP.xlsx", sheet_name = "2.1")

# Cambiar nombre de las columnas
ipp = ipp.rename(columns={'Ene-20': 'Enero 2020','Feb-20': 'Febrero 2020','Mar-20': 'Marzo 2020','Abr-20': 'Abril 2020','May-20': 'Mayo 2020','Jun-20': 'Junio 2020','Jul-20': 'Julio 2020','Ago-20': 'Agosto 2020','Sep-20': 'Septiembre 2020','Oct-20': 'Octubre 2020','Nov-20': 'Noviembre 2020','Dic-20': 'Diciembre 2020','ene-21 (pr)*': 'Enero 2021', 'feb-21 (pr)*': 'Febrero 2021', 'mar-21 (pr)*': 'Marzo 2021', 'abr-21 (pr)*': 'Abril 2021', 'May-21 (pr)*': 'Mayo 2021', 'Jun-21 (pr)*': 'Junio 2021', 'Jul-21 (pr)*': 'Julio 2021', 'Ago-21 (pr)*': 'Agosto 2021', 'Sep-21 (pr)*': 'Septiembre 2021', 'Oct-21 (pr)*': 'Octubre 2021', 'Nov-21 (pr)*': 'Noviembre 2021', 'Dic-21 (pr)*': 'Diciembre 2021','Ene-22 (pr)*': 'Enero 2022', 'Feb-22 (pr)*': 'Febrero 2022', 'Mar-22 (pr)*': 'Marzo 2022', 'Abr-22 (pr)*': 'Abril 2022', 'May-22 (pr)*': 'Mayo 2022', 'Jun-22 (pr)*': 'Junio 2022', 'Jul-22 (pr)*': 'Julio 2022', 'Ago-22 (pr)*': 'Agosto 2022', 'Sep-22 (pr)*': 'Septiembre 2022', 'Oct-22 (pr)*': 'Octubre 2022', 'Nov-22 (pr)*': 'Noviembre 2022', 'Dic-22 (pr)*': 'Diciembre 2022','Ene-23 (pr)*': 'Enero 2023', 'Feb-23 (pr)*': 'Febrero 2023', 'Mar-23 (pr)*': 'Marzo 2023', 'Abr-23 (pr)*': 'Abril 2023', 'May-23 (pr)*': 'Mayo 2023', 'Jun-23 (pr)*': 'Junio 2023', 'Jul-23 (pr)*': 'Julio 2023', 'Ago-23 (pr)*': 'Agosto 2023', 'Sep-23 (pr)*': 'Septiembre 2023', 'Oct-23 (pr)*': 'Octubre 2023'})


#st.write(ipp)

#Traer el IPP
IPPm_1 = ipp[año_mes][0]
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

IPCm_1 = ipc["Índice"][año_mes] #Se trae el IPC del mes que se quiere calcular
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