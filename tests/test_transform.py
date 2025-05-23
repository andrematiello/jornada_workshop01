import pandas as pd
import numpy as np
from app.pipeline.transform import transform_data

def test_transform_data():
    # ✅ Arrange
    data = {
        'col1': [1, 2, 3, np.nan],
        'col2': [4.0, 5.0, 6.0, 7.0],
        'col3': ['a', 'b', 'c', 'd'],
    }
    df = pd.DataFrame(data)

    # ✅ Act
    result = transform_data(df)

    # ✅ Assert
    # Deve ter removido a linha com NaN
    assert result.shape[0] == 3
    # col1 normalizada entre 0 e 1
    assert result['col1'].min() == 0
    assert result['col1'].max() == 1
    # col2 normalizada entre 0 e 1
    assert result['col2'].min() == 0
    assert result['col2'].max() == 1
