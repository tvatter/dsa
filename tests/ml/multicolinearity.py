import numpy as np
import pandas as pd
from patsy import dmatrix
from statsmodels.stats.outliers_influence import \
    variance_inflation_factor as vif

df = pd.read_csv('tests/ml/data/bmi.csv').drop(
    labels=['Index'],
    axis=1).assign(Gender=lambda df: np.where(df['Gender'] == 'Male', 1, 0))

vif_data = pd.DataFrame({
    'feature': df.columns,
    'vif': [vif(df.values, i) for i in range(df.shape[1])]
})

print(vif_data)  # Obviously vif for Height/Weight is high :)
