def lcs_recurs(s1, s2):

  x = s1[-1]
  y = s2[-1]

  if len(s1) == 1:
    if x in s2:
      return x
    else:
      return ''

  if len(s2) == 1:
    if y in s1:
      return y
    else:
      return ''

  if x == y:
    return lcs_recurs(s1[:-1], s2[:-1]) + x
  else:
    l1 = lcs_recurs(s1[:-1], s2)
    l2 = lcs_recurs(s1, s2[:-1])
    if len(l1) > len(l2):
      return l1
    else:
      return l2

# Slightly different from CLRS (MINE haha)
def lcs_dp(s1, s2):
  ll = [[None] * len(s2) for _ in range(len(s1))]

  def lcs_dp_aux(i, j):
    x = s1[i]
    y = s2[j]

    if i == 0:
      output = x if x in s2[:j] else ''
    elif j == 0:
      output = y if y in s1[:i] else ''
    else:
      if x == y:
        output = ll[i-1][j-1] + x
      else:
        l1 = ll[i - 1][j]
        l2 = ll[i][j - 1]
        output = l1 if len(l1) > len(l2) else l2
    return output

  for i in range(len(s1)):
    for j in range(len(s2)):
      ll[i][j] = lcs_dp_aux(i, j)

  return lcs_dp_aux(len(s1) - 1, len(s2) - 1)


s1 = 'ABCBDAB'
s2 = 'BDCABA'
len(lcs_recurs(s1, s2)) == 4
lcs_dp(s1, s2)

%timeit lcs_recurs(s1, s2)
%timeit lcs_dp(s1, s2)

s1 = 'ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'
s2 = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'
s3 = 'GTCGTCGGAAGCCGGCCGAA'
# lcs_recurs(s1, s2) # doesn't end on my laptop
solution = lcs_dp(s1, s2)
solution == s3

