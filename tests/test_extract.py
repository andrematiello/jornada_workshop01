import pytest
from unittest import mock
import pandas as pd
from app.pipeline.extract import read_excel_files
from app.pipeline.transform import transform_data


def test_read_excel_files(monkeypatch):
    # ✅ Arrange
    input_path = "dummy_path"
    dummy_files = ['file1.xlsx', 'file2.xlsx']
    dummy_df1 = pd.DataFrame({'col': [1, 2]})
    dummy_df2 = pd.DataFrame({'col': [3, 4]})

    # Mock glob.glob para retornar arquivos fictícios
    monkeypatch.setattr('glob.glob', lambda pattern: dummy_files)

    # Mock pd.read_excel para retornar DataFrames fictícios
    with mock.patch('pandas.read_excel', side_effect=[dummy_df1, dummy_df2]):
        # ✅ Act
        result = read_excel_files(input_path)

        # ✅ Assert
        expected_df = pd.concat([dummy_df1, dummy_df2], ignore_index=True)
        pd.testing.assert_frame_equal(result, expected_df)
