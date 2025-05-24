# import os
# import pandas as pd
# import pyarrow as pa
# import pyarrow.parquet as pq

# """
# Módulo de transformação de dados.
# Inclui funções para transformação de DataFrame e conversão para Parquet.
# """

# def transform_data(df: pd.DataFrame) -> pd.DataFrame:
#     """
#     Transforma o DataFrame: remove NaN e normaliza colunas numéricas.

#     Parâmetros:
#         df (pd.DataFrame): DataFrame de entrada.

#     Retorno:
#         pd.DataFrame: DataFrame transformado.
#     """
#     print("🔹 Iniciando transformação de dados...")
    

#     # Remove linhas com valores nulos
#     df = df.dropna().copy()
#     print(f"✅ Linhas após remoção de NaN: {len(df)}")

#     # Seleciona colunas numéricas
#     numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
#     print(f"🔹 Colunas numéricas identificadas: {list(numeric_cols)}")

#     # Converte explicitamente para float
#     df = df.astype({col: float for col in numeric_cols})

#     # Normaliza colunas numéricas
#     df_normalized = df[numeric_cols].apply(
#         lambda x: (x - x.min()) / (x.max() - x.min()) if x.max() != x.min() else 0
#     )
#     df.loc[:, numeric_cols] = df_normalized

#     print("✅ Transformação concluída.")
#     return df

# def convert_df_to_parquet(df: pd.DataFrame, output_path: str) -> None:
#     """
#     Converte um DataFrame para Parquet e salva na pasta especificada.

#     Parâmetros:
#         df (pd.DataFrame): DataFrame de entrada.
#         output_path (str): Caminho do arquivo Parquet de saída.

#     Retorno:
#         None
#     """
#     try:
#         print(f"🔹 Convertendo DataFrame para Parquet em {output_path}...")
#         os.makedirs(os.path.dirname(output_path), exist_ok=True)

#         table = pa.Table.from_pandas(df)
#         pq.write_table(table, output_path)

#         print("✅ Arquivo convertido com sucesso para Parquet.")
#     except Exception as e:
#         print(f"❌ Erro ao converter o arquivo: {e}")



        
        
        
        
        
import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import unicodedata

"""
Módulo de transformação de dados.
Inclui funções para transformação de DataFrame e conversão para Parquet.
"""

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza os nomes das colunas: minúsculas, sem acentos, underscores no lugar de espaços.
    """
    print("🔹 Padronizando nomes das colunas...")

    def remove_accents(input_str: str) -> str:
        nfkd = unicodedata.normalize('NFKD', input_str)
        return "".join([c for c in nfkd if not unicodedata.combining(c)])

    new_columns = []
    for col in df.columns:
        col_new = remove_accents(col)
        col_new = col_new.lower()
        col_new = col_new.replace(" ", "_")
        new_columns.append(col_new)

    df.columns = new_columns
    print(f"✅ Novos nomes das colunas: {list(df.columns)}")
    return df

def remove_na_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove linhas com valores nulos do DataFrame.
    """
    print("🔹 Removendo linhas com valores nulos...")
    df_clean = df.dropna().copy()
    print(f"✅ Linhas restantes após remoção de NaN: {len(df_clean)}")
    return df_clean

def clean_name_prefixes(df: pd.DataFrame, column: str = "colaborador_nome") -> pd.DataFrame:
    """
    Remove prefixos de tratamento como Sr., Sra., Dr., Dra. do nome.
    """
    if column in df.columns:
        print(f"🔹 Removendo prefixos de tratamento de nomes na coluna '{column}'...")
        df[column] = df[column].str.replace(r"^(Sr\.|Sra\.|Dr\.|Dra\.|Srta\.)\s*", "", regex=True)
        print(f"✅ Prefixos removidos da coluna: {column}")
    else:
        print(f"⚠️ Coluna '{column}' não encontrada. Nenhuma alteração feita.")
    return df

def split_datetime_column(df: pd.DataFrame, column: str = "data_da_ausencia") -> pd.DataFrame:
    """
    Separa coluna datetime em duas: data e hora. E renomeia a original para 'data_ausencia'.
    """
    if column in df.columns:
        print(f"🔹 Separando data e hora da coluna '{column}'...")
        df[column] = pd.to_datetime(df[column])
        df['data'] = df[column].dt.date
        df['hora'] = df[column].dt.time
        df = df.rename(columns={column: 'data_ausencia'})
        print(f"✅ Coluna '{column}' separada e renomeada para 'data_ausencia'.")
    else:
        print(f"⚠️ Coluna '{column}' não encontrada. Nenhuma alteração feita.")
    return df

def format_salary(df: pd.DataFrame, column: str = "salario") -> pd.DataFrame:
    """
    Formata a coluna de salário como string no padrão monetário R$.
    """
    if column in df.columns:
        print(f"🔹 Formatando coluna de salário '{column}'...")
        df[column] = df[column].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"✅ Coluna '{column}' formatada como monetária.")
    else:
        print(f"⚠️ Coluna '{column}' não encontrada. Nenhuma alteração feita.")
    return df

def convert_numeric_to_float(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte colunas numéricas do DataFrame para tipo float.
    """
    print("🔹 Convertendo colunas numéricas para float...")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df = df.astype({col: float for col in numeric_cols})
    print(f"✅ Colunas convertidas: {list(numeric_cols)}")
    return df

def exclude_columns_from_normalization(df: pd.DataFrame, exclude: list) -> pd.DataFrame:
    """
    Normaliza colunas numéricas, exceto as listadas.
    """
    print("🔹 Normalizando colunas numéricas (exceto as excluídas)...")

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    cols_to_normalize = [col for col in numeric_cols if col not in exclude]

    for col in cols_to_normalize:
        min_val = df[col].min()
        max_val = df[col].max()
        if max_val != min_val:
            df[col] = (df[col] - min_val) / (max_val - min_val)
            print(f"✅ Coluna '{col}' normalizada.")
        else:
            df[col] = 0
            print(f"⚠️ Coluna '{col}' possui valores constantes. Normalizada como 0.")

    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma o DataFrame: padroniza nomes de colunas, remove NaN, ajusta nomes, separa datas,
    formata salário, converte colunas numéricas e normaliza com exclusões.
    """
    print("🔹 Iniciando transformação de dados...")

    df = standardize_column_names(df)
    df = remove_na_rows(df)
    df = clean_name_prefixes(df, column='colaborador_nome')
    df = split_datetime_column(df, column='data_da_ausencia')
    df = format_salary(df, column='salario')
    df = convert_numeric_to_float(df)
    df = exclude_columns_from_normalization(df, exclude=['colaborador_id', 'horas_de_ausencia'])

    print("✅ Transformação concluída.")
    return df

def convert_df_to_parquet(df: pd.DataFrame, output_path: str) -> None:
    """
    Converte um DataFrame para Parquet e salva na pasta especificada.
    """
    try:
        print(f"🔹 Convertendo DataFrame para Parquet em {output_path}...")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        table = pa.Table.from_pandas(df)
        pq.write_table(table, output_path)

        print("✅ Arquivo convertido com sucesso para Parquet.")
    except Exception as e:
        print(f"❌ Erro ao converter o arquivo: {e}")
