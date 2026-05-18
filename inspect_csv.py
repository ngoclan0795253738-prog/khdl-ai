import pandas as pd
import os
path = 'dữ liệu lớn.csv'
print('exists', os.path.exists(path))
try:
    df = pd.read_csv(path)
    print(df.shape)
    print(df.columns.tolist())
    print(df.head(10).to_string(index=False))
except Exception as e:
    print('ERROR', e)
