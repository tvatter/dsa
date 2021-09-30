def triple_step_recurs(n):
  if n < 0:
    return 0
  elif n  == 0:
    return 1
  else:
    return triple_step_recurs(n - 3) + triple_step_recurs(
        n - 2) + triple_step_recurs(n - 1)


def triple_step_dp(n):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    a, b, c = 1, 2, 4
    for _ in range(4, n + 1):
      d = a + b + c
      a, b, c = b, c, d
    return d


triple_step_recurs(4)
triple_step_dp(4)

triple_step_recurs(6)
triple_step_dp(6)

%timeit triple_step_recurs(10)
%timeit triple_step_dp(10)
