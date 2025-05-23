import pandas as pd
from unittest import mock
from app.pipeline.extract import extract_from_excel

def test_extract_from_excel(monkeypatch):
    # ✅ Arrange
    input_path = 'dummy_path'
    dummy_files = ['dummy_path/file1.xlsx', 'dummy_path/file2.xlsx']
    dummy_df1 = pd.DataFrame({'col': [1, 2]})
    dummy_df2 = pd.DataFrame({'col': [3, 4]})

    # Mock glob.glob para simular arquivos encontrados
    monkeypatch.setattr('glob.glob', lambda pattern: dummy_files)

    # Mock pd.read_excel para retornar DataFrames fictícios
    with mock.patch('pandas.read_excel', side_effect=[dummy_df1, dummy_df2]):
        # ✅ Act
        result = extract_from_excel(input_path)

        # ✅ Assert
        expected_df = pd.concat([dummy_df1, dummy_df2], ignore_index=True)
        pd.testing.assert_frame_equal(result, expected_df)

