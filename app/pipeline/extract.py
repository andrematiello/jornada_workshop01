import os
import glob
import pandas as pd

"""
Módulo de extração de dados.
Funções para ler múltiplos arquivos Excel e retornar um DataFrame concatenado.
"""

def extract_from_excel(input_path: str) -> pd.DataFrame:
    """
    Função para extrair dados de arquivos Excel de uma pasta e retornar um DataFrame concatenado.

    Parâmetros:
        input_path (str): Caminho da pasta contendo arquivos .xlsx.

    Retorno:
        pd.DataFrame: DataFrame único com todos os dados concatenados.
    """
    dfs = []
    
    for file in glob.glob(os.path.join(input_path, '*.xlsx')):
        print(f"🔹 Lendo arquivo: {file}")
        df = pd.read_excel(file)
        dfs.append(df)
    
    if not dfs:
        print(f"⚠️ Nenhum arquivo .xlsx encontrado em {input_path}.")
        return pd.DataFrame()  # Retorna DataFrame vazio
    
    df_concat = pd.concat(dfs, ignore_index=True)
    print(f"✅ {len(dfs)} arquivos concatenados com sucesso.")
    
    return df_concat
