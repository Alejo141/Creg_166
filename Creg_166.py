import streamlit as st
import pandas as pd

import pip
pip.main(["install", "openpyxl"])

st.title("Cálculos CREG 166")

Gi0 = 0
Gaom0 = 86525
C0 = 23181
IPP0 = 122.59
IPC0 = 104.97

G0 = Gi0 + Gaom0
st.code(G0)

ipp = pd.read_excel("IPP.xlsx", sheet_name = "2.1")
st.write(ipp)

st.code(ipp["May-23 (pr)*"])

IPPm_1 = ipp["May-23 (pr)*"][0]

st.caption("IPPm_1:")
st.code(IPPm_1)

Gm = G0 * (IPPm_1/IPP0)
st.code(Gm)

df = pd.read_excel("IPC.xlsx")
st.write(df)

ipc = df.set_index("Año(aaaa)-Mes(mm)")
st.write(ipc)

IPCm_1 = ipc["Índice"][202307]

st.caption("IPCm_1:")
st.code(IPCm_1)

Cm = C0 * (IPCm_1/IPC0)
st.code(Cm)

CU = Gm + Cm
st.code(CU)