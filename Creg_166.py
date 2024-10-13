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

df = pd.read_excel("IPP.xlsx", sheet_name = "2.1")
st.write(df)

#st.code(df["May-23 (pr)*"])

IPPm_1 = df["May-23 (pr)*"][0]

st.code(IPPm_1)