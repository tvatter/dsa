from string import ascii_letters

import numpy as np
import pandas as pd

# Create random df with two columns
n = 10 ** 6
df = pd.DataFrame(
  {
    l: np.random.rand(n) for l in ascii_lowercase
  }
)
df.info(memory_usage='deep')

# Suppose one wants to sum columns x and y
# A dumb (non-vectorized) method would be to use a loop
def dumb_sum(df):
  n_rows = df.shape[0]
  output = np.empty((n_rows, 1))
  for i in range(df.shape[0]):
    output[i] = df.iloc[i,0] + df.iloc[i,1]
  return output

# Dumb loop
%timeit df['z'] = dumb_sum(df)

# Vectorized operations are several orders of magnitude faster
%timeit df['z'] = df['x'] + df['y']

# Adds a column and return a copy 
%timeit df.assign(z=lambda row: row.x + row.y)

# Adds a column only
%timeit df.assign(z=lambda row: row.x + row.y, inplace=True)

n = 10 ** 7
df = pd.DataFrame(
  {
    l: np.random.rand(n) for l in ascii_letters
  }
)
df.info(memory_usage='deep')
%timeit df['z'] = df['x'] + df['y']
%timeit df.assign(z=lambda row: row.x + row.y)
%timeit df.assign(z=lambda row: row.x + row.y, inplace=True)

import numpy as np
import pandas as pd

n = 10 ** 7
df = pd.DataFrame(
  {
    'x': np.random.randn(n),
    'y': np.random.randn(n)
  }
)
%timeit df['z'] = df['x'] + df['y']
%timeit df.assign(z=lambda row: row.x + row.y)
%timeit df.assign(z=lambda row: row.x + row.y, inplace=True)
