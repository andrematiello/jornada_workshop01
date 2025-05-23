import os
import pandas as pd

"""
Módulo de carga de dados.
Inclui funções para leitura de arquivos Parquet e exportação para Excel.
"""

def load_parquets(input_dir: str) -> pd.DataFrame:
    """
    Lê todos os arquivos Parquet de um diretório e retorna um DataFrame concatenado.

    Parâmetros:
        input_dir (str): Caminho para o diretório contendo arquivos Parquet.

    Retorno:
        pd.DataFrame: DataFrame concatenado.
    """
    dfs = []

    for file in os.listdir(input_dir):
        if file.endswith('.parquet'):
            file_path = os.path.join(input_dir, file)
            print(f"🔹 Lendo arquivo Parquet: {file_path}")
            df = pd.read_parquet(file_path)
            dfs.append(df)

    if not dfs:
        print(f"⚠️ Nenhum arquivo Parquet encontrado em {input_dir}.")
        return pd.DataFrame()

    df_concat = pd.concat(dfs, ignore_index=True)
    print(f"✅ {len(dfs)} arquivos Parquet concatenados com sucesso.")
    return df_concat

def save_to_excel(df: pd.DataFrame, output_path: str, sheet_name: str = 'files_loaded', index: bool = True) -> None:
    """
    Salva um DataFrame em um arquivo Excel.

    Parâmetros:
        df (pd.DataFrame): DataFrame a ser salvo.
        output_path (str): Caminho para salvar o arquivo Excel.
        sheet_name (str): Nome da aba no arquivo Excel.
        index (bool): Indica se deve incluir o índice no arquivo Excel.

    Retorno:
        None
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        print(f"🔹 Salvando DataFrame em Excel: {output_path} (sheet: {sheet_name}, index: {index})")
        df.to_excel(output_path, sheet_name=sheet_name, index=index)
        print(f"✅ Arquivo salvo com sucesso em: {output_path}")
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo Excel: {e}")
