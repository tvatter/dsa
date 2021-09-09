def bin_to_string(num):
  cnt = 0
  res = '.'
  while num > 0:
    if (cnt >= 32):
      return 'ERROR'
    cnt += 1
    digit, num = divmod(num * 2, 1)
    res += str(int(digit))

  return res


bin_to_string(0.72)
bin_to_string(0.625)
