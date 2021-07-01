def is_permutation(s1, s2):
  n = len(s1)
  if len(s2) != n:
    return False

  s_array = [0 for _ in range(128)]
  for x in s1:
    i = ord(x)
    s_array[i] += 1

  for x in s2:
    i = ord(x)
    s_array[i] -= 1
    if s_array[i] < 0:
      return False

  return True


if __name__ == '__main__':

  from icecream import ic
  ic(is_permutation('abc  ', 'abc'))
  ic(is_permutation('abc  ', '  abc'))
  ic(is_permutation('ab c', 'C ba'))
  ic(is_permutation('ab c', 'c ba'))
  ic(is_permutation('abc', 'cca'))

# def is_permutation(s1, s2):
#   n = len(s1)
#   if len(s2) != n:
#     return False

#   d1 = {x: 0 for x in string.printable}
#   d2 = d1.copy()
#   for i in range(n):
#     d1[s1[i]] += 1
#     d2[s2[i]] += 1

#   for x in string.printable:
#     if d1[x] != d2[x]:
#       return False

#   return True
