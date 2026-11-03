import streamlit as st
import pandas as pd

st.title("Kit de Extração do Google Maps")
termo = st.text_input("O que deseja procurar? (ex: oficinas em Sao Paulo)")

if st.button("Iniciar Extração"):
    st.write(f"A iniciar extração para: {termo}...")
    
    # Exemplo de dados obtidos (substitua pelo DataFrame ou ficheiro gerado pelo seu script)
    dados = {
        "Nome": ["Empresa Exemplo A", "Empresa Exemplo B"],
        "Morada": ["Rua 1, Potirendaba", "Rua 2, Rio Preto"],
        "Telefone": ["(17) 99999-9999", "(17) 88888-8888"]
    }
    df = pd.DataFrame(dados)
    
    # Converter os dados para formato CSV
    csv_data = df.to_csv(index=False).encode('utf-8')
    
    st.success("Processo concluído!")
    
    # Botão que aparecerá na página para descarregar o ficheiro
    st.download_button(
        label="Descarregar dados extraídos (CSV)",
        data=csv_data,
        file_name="resultados_google_maps.csv",
        mime="text/csv"
    )
