def has_all_unique(s):
  if len(s) > 128:
    return False
  char_set = [False for _ in range(128)]
  for x in s:
    i = ord(x)
    if not char_set[i]:
      char_set[i] = True
    else:
      return False
  return True


if __name__ == '__main__':

  from icecream import ic
  ic(has_all_unique('abc'))
  ic(has_all_unique('aabc'))
  ic(has_all_unique('abca'))
  ic(has_all_unique('abc\x00'))
  ic(has_all_unique('a\x00bc\x00'))
