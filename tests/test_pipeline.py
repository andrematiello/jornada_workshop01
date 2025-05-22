"""
O que é esse teste?
Não testa funções isoladas, mas sim o fluxo completo:
Ler Excel → Transformar dados → Verificar resultado final.

Ainda pode seguir a estrutura AAA (Arrange, Act, Assert).
"""

import pytest
import pandas as pd
from unittest import mock
from app.pipeline.extract import read_excel_files
from app.pipeline.transform import transform_data


def test_pipeline(monkeypatch):
    # ✅ Arrange
    input_path = "dummy_path"
    dummy_files = ['file1.xlsx', 'file2.xlsx']
    
    dummy_df1 = pd.DataFrame({'col1': [1, 2], 'col2': [10.0, 20.0]})
    dummy_df2 = pd.DataFrame({'col1': [3, 4], 'col2': [30.0, 40.0]})

    # Mock glob para simular arquivos
    monkeypatch.setattr('glob.glob', lambda pattern: dummy_files)
    # Mock pd.read_excel para retornar DataFrames fictícios
    with mock.patch('pandas.read_excel', side_effect=[dummy_df1, dummy_df2]):
        # ✅ Act
        df_raw = read_excel_files(input_path)
        df_transformed = transform_data(df_raw)

        # ✅ Assert
        # Garantir que concatenação deu certo
        assert df_raw.shape == (4, 2)
        # Garantir que não existem NaNs após transformação
        assert not df_transformed.isnull().values.any()
        # Garantir que normalizou entre 0 e 1
        for col in ['col1', 'col2']:
            assert df_transformed[col].min() == 0
            assert df_transformed[col].max() == 1

