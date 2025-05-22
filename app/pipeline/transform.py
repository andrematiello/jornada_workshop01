"""
Transforma um arquivo CSV em Parquet e salva na pasta especificada.
Args:
    input_path (str): Caminho do arquivo CSV de entrada.
    output_path (str): Caminho do arquivo Parquet de saída.
"""

import os  # Módulo para manipular caminhos e diretórios
import pandas as pd  # Biblioteca para manipulação de dados tabulares
import pyarrow as pa  # Biblioteca para estrutura de dados colunares
import pyarrow.parquet as pq  # Para escrever arquivos Parquet

def transform_csv_to_parquet(input_path: str, output_path: str) -> None:
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(input_path)

        # Garante que o diretório de saída existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Converte o DataFrame para Parquet
        table = pa.Table.from_pandas(df)
        pq.write_table(table, output_path)

        print('Arquivo convertido com sucesso para Parquet')

    except Exception as e:
        print(f'Erro ao converter o arquivo: {e}')

"""
Transforma um DataFrame: remove NaN e normaliza colunas numéricas.
Args: df (pd.DataFrame): DataFrame de entrada.
Returns: pd.DataFrame: DataFrame transformado.
"""

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Remove linhas com valores nulos e cria uma cópia explícita
    df = df.dropna().copy()

    # Seleciona colunas numéricas
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    # Converte explicitamente as colunas numéricas para float
    df = df.astype({col: float for col in numeric_cols})

    # Normaliza as colunas numéricas
    df_normalized = df[numeric_cols].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

    # Atribui o DataFrame normalizado de volta
    df.loc[:, numeric_cols] = df_normalized

    return df



# Bloco de execução direta: só roda quando o script for executado diretamente
if __name__ == "__main__":
    transform_csv_to_parquet(
        input_path='data/output/concatenated_data.csv',
        output_path='data/output/concatenated_data.parquet'
    )

