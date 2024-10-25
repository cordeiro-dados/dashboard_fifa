import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0 ]
    df_Data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.write("# FIFA Dataset")
st.sidebar.markdown("Desenvolvido por Gabriel Cordeiro")

btn = st.button("Acesse os Dados do Kaggle")
if btn:
    webbrowser.open_new_tab("https://linkedin.com.br")

st.markdown("Conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de gutebol profissionais.")
