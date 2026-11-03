import streamlit as st
import subprocess
import os

st.title("Painel de Extração - Google Maps")

st.markdown("Insira os parâmetros abaixo para iniciar a busca e extração de leads.")

# Campos de entrada na interface do Streamlit
termo_busca = st.text_input("Termo de Pesquisa (ex: Dentistas, Restaurantes)", "Dentistas em Potirendaba")
localidade = st.text_input("Localização", "São José do Rio Preto, SP")
limite_resultados = st.slider("Número máximo de resultados", 10, 100, 20)

if st.button("Iniciar Extração"):
    with st.spinner("A executar o scraper... Por favor, aguarde."):
        try:
            # Exemplo de chamada ao script em Python do seu motor de scraping
            # Ajuste o comando conforme o script principal do seu repositório (ex: engine/maps.py)
            comando = ["python", "engine/maps.py", "--query", termo_busca, "--location", localidade, "--limit", str(limite_resultados)]
            
            resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
            
            st.success("Extração concluída com sucesso!")
            st.text_area("Log de Execução", resultado.stdout, height=200)
            
            # Se o scraper gerar um ficheiro CSV/Excel, disponibilize-o para download
            # if os.path.exists("output.csv"):
            #     with open("output.csv", "rb") as f:
            #         st.download_button("Descarregar Resultados (CSV)", f, file_name="leads.csv", mime="text/csv")
                    
        except subprocess.CalledProcessError as e:
            st.error(f"Ocorreu um erro durante a execução do scraper:")
            st.text_area("Erro", e.stderr, height=150)
