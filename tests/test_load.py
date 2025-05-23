import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
import tempfile
from app.pipeline.load import load_parquets, save_to_excel

def test_load_parquets_and_save_to_excel(tmp_path):
    # ✅ Arrange
    # Criar DataFrame de exemplo
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    
    # Criar diretório temporário para Parquet
    parquet_dir = tmp_path / "parquet_files"
    parquet_dir.mkdir()
    
    # Salvar como Parquet
    parquet_file = parquet_dir / "test.parquet"
    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_file)
    
    # ✅ Act
    df_loaded = load_parquets(str(parquet_dir))

    # ✅ Assert - ver se carregou corretamente
    pd.testing.assert_frame_equal(df, df_loaded)

    # ✅ Act - salvar como Excel
    excel_output = tmp_path / "output.xlsx"
    save_to_excel(df_loaded, str(excel_output))

    # ✅ Assert - verificar se arquivo foi criado
    assert os.path.exists(excel_output), "Arquivo Excel não foi criado"
