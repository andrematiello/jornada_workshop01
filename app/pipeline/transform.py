import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

"""
Módulo de transformação de dados.
Inclui funções para transformação de DataFrame e conversão para Parquet.
"""

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma o DataFrame: remove NaN e normaliza colunas numéricas.

    Parâmetros:
        df (pd.DataFrame): DataFrame de entrada.

    Retorno:
        pd.DataFrame: DataFrame transformado.
    """
    print("🔹 Iniciando transformação de dados...")

    # Remove linhas com valores nulos
    df = df.dropna().copy()
    print(f"✅ Linhas após remoção de NaN: {len(df)}")

    # Seleciona colunas numéricas
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    print(f"🔹 Colunas numéricas identificadas: {list(numeric_cols)}")

    # Converte explicitamente para float
    df = df.astype({col: float for col in numeric_cols})

    # Normaliza colunas numéricas
    df_normalized = df[numeric_cols].apply(
        lambda x: (x - x.min()) / (x.max() - x.min()) if x.max() != x.min() else 0
    )
    df.loc[:, numeric_cols] = df_normalized

    print("✅ Transformação concluída.")
    return df

def convert_df_to_parquet(df: pd.DataFrame, output_path: str) -> None:
    """
    Converte um DataFrame para Parquet e salva na pasta especificada.

    Parâmetros:
        df (pd.DataFrame): DataFrame de entrada.
        output_path (str): Caminho do arquivo Parquet de saída.

    Retorno:
        None
    """
    try:
        print(f"🔹 Convertendo DataFrame para Parquet em {output_path}...")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        table = pa.Table.from_pandas(df)
        pq.write_table(table, output_path)

        print("✅ Arquivo convertido com sucesso para Parquet.")
    except Exception as e:
        print(f"❌ Erro ao converter o arquivo: {e}")
