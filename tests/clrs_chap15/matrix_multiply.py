from functools import reduce

import numpy as np


# Dynamic programming solution from CLRS 15.2
def matrix_chain_order(p):
  n = len(p) - 1
  m = np.zeros(shape=[n, n])
  s = np.zeros(shape=[n, n])
  for l in range(2, n + 1):
    for i in range(0, n - l + 1):
      j = i + l - 1
      m[i, j] = np.Inf
      for k in range(i, j):
        q = m[i, k] + m[k + 1, j] + p[i] * p[k + 1] * p[j + 1]
        if q < m[i, j]:
          m[i, j] = q
          s[i, j] = k
  m = m.astype(int)
  s = s.astype(int)
  return m, s

# Print the optimal parenthesisation
def optimal_parenthesis(s, i, j, print=True):
  if i == j:
    return 'A{}'.format(i + 1)
  else:
    return '({}{})'.format(optimal_parenthesis(s, i, s[i, j]),
                            optimal_parenthesis(s, s[i, j] + 1, j))

# "Dumb" chain_multiply
def chain_multiply(arrays): 
  return reduce(np.dot, arrays)

# Recursive chain_multiply using the DP optimal solution
def chain_multiply_dp(arrays):
  p = [x.shape[0] for x in arrays]
  p.append(arrays[-1].shape[1])
  m, s = matrix_chain_order(p)

  def chain_multiply_dp_aux(i, j):
    if i == j:
      return arrays[i]
    else:
      return np.dot(chain_multiply_dp_aux(i, s[i, j]),
                       chain_multiply_dp_aux(s[i, j] + 1, j))

  return chain_multiply_dp_aux(0, len(p) - 2)

# To generate a bunch of random arrays for benchmarking
def generate_arrays(p):
  rng = np.random.default_rng()
  return [rng.random((dim1, dim2)) for dim1, dim2 in zip(p[:-1], p[1:])]

# Stuff from CLRS
p = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain_order(p)
m[0, 5] # min number of scalar multiplications
optimal_parenthesis(s, 0, 5) # optimal parenthesisation

# Try to do the actual multiplications with random arrays
arrays_random = generate_arrays(p)

prod0 = chain_multiply(arrays_random)
prod1 = np.linalg.multi_dot(arrays_random)
prod2 = chain_multiply_dp(arrays_random)
np.linalg.norm(prod0 - prod1) # floating point precision
np.linalg.norm(prod1 - prod2)

# Increase the dimension for benchmarking
p10 = [x * 10 for x in p]
arrays_random = generate_arrays(p10)

%timeit chain_multiply(arrays_random)
%timeit np.linalg.multi_dot(arrays_random)
%timeit chain_multiply_dp(arrays_random)

