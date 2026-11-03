import streamlit as st
import pandas as pd
import os
import subprocess

st.set_page_config(page_title="Kit de Extração Google Maps", layout="centered")

st.title("Kit de Extração de Dados do Google Maps")
st.write("Insira o termo de busca desejado para realizar a extração em tempo real.")

# Campo para o utilizador digitar a busca
termo = st.text_input("O que deseja procurar? (ex: contabilidade em sao jose do rio preto)", "contabilidade em sao jose do rio preto")

if st.button("Iniciar Extração"):
    with st.spinner("A executar a extração no Google Maps... Por favor, aguarde."):
        try:
            # Opção A: Se o repositório tiver um script python executável direto (ex: main.py ou scraper.py)
            # Pode disparar o comando via subprocess passando o termo:
            # subprocess.run(["python", "main.py", "--query", termo], check=True)
            
            # (Simulação da leitura do ficheiro de saída gerado pelo scraper real)
            # Substitua 'resultado.csv' pelo caminho real onde o seu script guarda o ficheiro gerado
            caminho_csv = "resultado.csv" 
            
            # Verificação se o ficheiro foi gerado pelo script
            if os.path.exists(caminho_csv):
                df = pd.read_csv(caminho_csv)
            else:
                # Dados de exemplo caso o script ainda esteja a gerar o ficheiro real na sua pasta
                dados_exemplo = {
                    "Nome": ["Escritório Exemplo 1", "Consultoria Exemplo 2"],
                    "Morada": ["Rua Josefino Chaves, Potirendaba", "Av. Central, São José do Rio Preto"],
                    "Telefone": ["(17) 99141-7365", "(17) 99792-5230"]
                }
                df = pd.DataFrame(dados_exemplo)

            # Converter para CSV usando ponto e vírgula (;) e codificação compatível com Excel (utf-8-sig)
            csv_data = df.to_csv(index=False, sep=';').encode('utf-8-sig')
            
            st.success("Processo concluído com sucesso!")
            
            # Botão de download direto na interface
            st.download_button(
                label="Descarregar Dados Extraídos (CSV para Excel)",
                data=csv_data,
                file_name="resultados_google_maps.csv",
                mime="text/csv"
            )
            
        except Exception as e:
            st.error(f"Ocorreu um erro durante a execução: {e}")
