import os
import pandas as pd
import pytest

def test_pipeline_integration():
    # ✅ Arrange
    parquet_file = 'data/output/concatenated_data.parquet'
    excel_file = 'data/output/files_loaded.xlsx'
    
    # ✅ Act & Assert
    # 1. Verifica existência do arquivo Parquet
    assert os.path.exists(parquet_file), f"❌ Arquivo Parquet não encontrado: {parquet_file}"
    
    # 2. Verifica existência do arquivo Excel
    assert os.path.exists(excel_file), f"❌ Arquivo Excel não encontrado: {excel_file}"
    
    # 3. Verifica que o Excel tem dados
    df_excel = pd.read_excel(excel_file)
    assert not df_excel.empty, "❌ O arquivo Excel está vazio."
    
    print("\n✅ Pipeline executado com sucesso: todos os arquivos gerados e validados!")
