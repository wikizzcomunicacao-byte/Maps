import streamlit as st

st.title("Kit de Extração do Google Maps")
termo = st.text_input("O que deseja procurar? (ex: oficinas em Sao Paulo)")

if st.button("Iniciar Extração"):
    st.write(f"A iniciar extração para: {termo}...")
    # Aqui pode chamar a função principal do scraper do seu repositório
    st.success("Processo concluído!")
