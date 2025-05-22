import os  # Módulo para manipular caminhos e diretórios
import glob  # Módulo para buscar arquivos por padrão (ex.: *.xlsx)
import pandas as pd  # Biblioteca para manipulação de dados tabulares

"""
Função para ler os arquivos Excel de uma pasta e retornar um DataFrame concatenado.
Args: input_path (str): Caminho da pasta com os arquivos .xlsx.
Returns: pd.DataFrame: DataFrame único, concatenando todos os arquivos lidos.
"""

def read_excel_files(input_path):
    dfs = []  # Cria uma lista vazia para armazenar os DataFrames

    # Loop sobre todos os arquivos .xlsx encontrados na pasta
    for file in glob.glob(os.path.join(input_path, '*.xlsx')):
        df = pd.read_excel(file)  # Lê cada arquivo Excel em um DataFrame
        dfs.append(df)  # Adiciona o DataFrame à lista

    # Concatena todos os DataFrames da lista em um só, com novo índice
    return pd.concat(dfs, ignore_index=True)

"""
Função para ler os arquivos Excel e gravar um único CSV na pasta data/output.
Se a operação falhar, exibe mensagem de erro.
"""

def write_csv_file() -> None:
    try:
        df = read_excel_files('data/input')  # Lê e concatena os arquivos Excel
        # Escreve o DataFrame concatenado em um arquivo CSV
        df.to_csv('data/output/concatenated_data.csv', index=False)
        print('Arquivos lidos com sucesso')  # Mensagem de sucesso
    except Exception as e:
        # Em caso de erro, imprime a mensagem de exceção
        print(f'Erro ao ler os arquivos: {e}')


# Bloco de execução direta: só roda quando o script for executado diretamente
if __name__ == "__main__":
    write_csv_file()  # Chama a função principal


