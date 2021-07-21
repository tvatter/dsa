def max_subset_recurs(s, f):
  n = len(s) + 2
  indices = range(n)
  compatible_subsets = [[None] * n for _ in range(n)]
  s = [-1] + s
  s.append(f[-1] + 1)
  f = [-1] + f
  f.append(f[-1] + 1)

  def sel_ix(ix, i, j, f_i, s_j):
    return s[ix] >= f_i and f[ix] <= s_j and ix != i and ix != j

  def max_subset_recurs_aux(i, j):
    if compatible_subsets[i][j] is None:
      f_i = f[i]
      s_j = s[j]
      s_ij = [ix for ix in indices if sel_ix(ix,i, j, f_i, s_j)]
      compatible_subsets[i][j] = s_ij
    else:
      s_ij = compatible_subsets[i][j]

    out = 0
    activities = [i - 1, j - 1]
    if len(s_ij) == 0:
      return out, activities
    else:
      for k in s_ij:
        c_ik, a_ik = max_subset_recurs_aux(i, k)
        c_kj, a_kj = max_subset_recurs_aux(k, j)
        if out < c_ik + c_kj + 1:
          activities = a_ik
          activities.extend(a_kj[1:])
          out = c_ik + c_kj + 1

      return out, activities

  length, activities = max_subset_recurs_aux(0, n - 1)
  activities = activities[1:-1]
  return length, activities


def max_subset_dp(s, f):
  n = len(s) + 2
  indices = range(n)
  compatible_subsets = [[None] * n for _ in range(n)]
  costs = [[None] * n for _ in range(n)]
  activities = [[None] * n for _ in range(n)]
  s = [-1] + s
  s.append(f[-1] + 1)
  f = [-1] + f
  f.append(f[-1] + 1)

  def sel_ix(ix, i, j, f_i, s_j):
    return s[ix] >= f_i and f[ix] <= s_j and ix != i and ix != j

  def max_subset_dp_aux(i, j):
    if i == j:
      return 0, []
    if compatible_subsets[i][j] is None:
      f_i = f[i]
      s_j = s[j]
      s_ij = [ix for ix in indices if sel_ix(ix,i, j, f_i, s_j)]
      compatible_subsets[i][j] = s_ij
    else:
      s_ij = compatible_subsets[i][j]

    cost = 0
    activity = []
    if len(s_ij) > 0:
      for k in s_ij:
        c_ik = costs[i][k]
        c_kj = costs[k][j]
        a_ik = activities[i][k]
        a_kj = activities[k][j]
        if cost < c_ik + c_kj + 1:
          activity = list(set(a_ik) | set(a_kj))
          activity.append(k - 1)
          cost = c_ik + c_kj + 1

    return cost, activity

  for l in range(1, n):
    for i in range(0, n - l + 1):
      j = i + l - 1
      costs[i][j], activities[i][j] = max_subset_dp_aux(i, j)

  length, activities = max_subset_dp_aux(0, n - 1)
  return length, sorted(activities)

def max_subset_greedy_recurs(s, f):
  n = len(s) + 1
  s = [-1] + s
  f = [-1] + f

  def recurs_activity_selector(k, n):
    m = k + 1
    while m < n and s[m] < f[k]: # ﬁnd the ﬁrst activity in S_k to ﬁnish
      m += 1
    if m < n:
      return [m - 1] + recurs_activity_selector(m, n)
    else:
      return []

  activities = recurs_activity_selector(0, n)
  return len(activities), activities

def max_subset_greedy(s, f):
  n = len(s) + 1
  s = [-1] + s
  f = [-1] + f
  activities = [0]
  k = 1
  for m in range(2, n):
    if s[m] >= f[k]:
      activities.append(m - 1)
      k = m
  return len(activities), activities

s_test = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f_test = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
max_subset_recurs(s_test, f_test)
max_subset_dp(s_test, f_test)
max_subset_greedy_recurs(s_test, f_test)
max_subset_greedy(s_test, f_test)

from random import randint, sample

f_test = sorted(sample(range(1, 50), 20))
s_test = [randint(0, x - 1) for x in f_test]
max_subset_recurs(s_test, f_test)
max_subset_dp(s_test, f_test)
max_subset_greedy_recurs(s_test, f_test)
max_subset_greedy(s_test, f_test)


%timeit max_subset_recurs(s_test, f_test)
%timeit max_subset_dp(s_test, f_test)
%timeit max_subset_greedy_recurs(s_test, f_test)
%timeit max_subset_greedy(s_test, f_test)
