import streamlit as st
import pandas as pd

import pip
pip.main(["install", "openpyxl"])

######### Título Pag ###########
st.title("Cálculos CREG 166")

######### Constantes ###########

st.subheader("Indique si es o no con inversión pública")
st.radio('Modulo, Estructura, OE y OC', ['Si'], ['No'])


Gi0 = 0
Gaom0 = 86525
C0 = 23181
IPP0 = 122.59
IPC0 = 104.97

######### Cálculo G0 ###########
G0 = Gi0 + Gaom0
st.caption("G0:")
st.code(G0)

######### Cargar excel IPP (Se deberá actualizar todos los meses ###########
ipp = pd.read_excel("IPP.xlsx", sheet_name = "2.1")
st.write(ipp)

#st.code(ipp["May-23 (pr)*"])

IPPm_1 = ipp["May-23 (pr)*"][0] #Se trae el IPP del mes que se quiere calcular

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