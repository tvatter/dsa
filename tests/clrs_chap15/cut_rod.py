def cut_rod_recurs(p, n):
  if n == 0:
    return 0
  q = -1 * float('inf')
  for i in range(n):
    q = max(q, p[i] + cut_rod_recurs(p, n - i - 1))
  return q


def cut_rod_memoized(p, n):
  r = [-1 * float('inf')] * n

  def cut_rod_memoized_aux(p, n, r):
    if r[n - 1] >= 0:
      return r[n - 1]
    if n == 0:
      q = 0
    else:
      q = -1 * float('inf')
      for i in range(n):
        q = max(q, p[i] + cut_rod_memoized_aux(p, n - i - 1, r))
    r[n - 1] = q
    return q

  return cut_rod_memoized_aux(p, n, r)

def cut_rod_bottom_up(p, n):
  r = [None] * (n + 1)
  r[0] = 0
  for j in range(1, n+1):
    q = -1 * float('inf')
    for i in range(j):
      q = max(q, p[i] + r[j - i - 1])
    r[j] = q
  return r[n]

def cut_rod_bottom_up_extended(p, n):
  r = [None] * (n + 1)
  s = [None] * (n + 1)
  r[0] = 0
  for j in range(1, n+1):
    q = -1 * float('inf')
    for i in range(j):
      if q < p[i] + r[j - i - 1]:
        q = p[i] + r[j - i - 1]
        s[j] = i + 1
    r[j] = q
  return r, s

def cut_rod_print(p, n):
  r, s = cut_rod_bottom_up_extended(p, n)
  to_print = ''
  while n > 0:
    if to_print != '':
      to_print += ','
    to_print += str(s[n])
    n = n - s[n]
  print(to_print)

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
cut_rod_recurs(p, 8)
cut_rod_recurs(p, 9)
cut_rod_recurs(p, 10)

cut_rod_memoized(p, 8)
cut_rod_memoized(p, 9)
cut_rod_memoized(p, 10)

cut_rod_bottom_up(p, 8)
cut_rod_bottom_up(p, 9)
cut_rod_bottom_up(p, 10)

cut_rod_print(p, 8)
cut_rod_print(p, 9)
cut_rod_print(p, 10)

%timeit cut_rod_recurs(p, 10)
%timeit cut_rod_memoized(p, 10)
%timeit cut_rod_bottom_up(p, 10)
