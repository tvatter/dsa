def to_bin(num):
  num, digit = divmod(num, 2)
  res = str(int(digit))
  while num > 0:
    num, digit = divmod(num, 2)
    res += str(digit)
  return res[::-1]


def flip_bit_to_win(num):
  if num < 2:
    return 1
  num_bin = to_bin(num)
  if '0' not in num_bin:
    return len(num_bin)

  curr_len = 0
  prev_len = 0
  max_len = 1

  while num != 0:
    if (num & 1) == 1:
      curr_len += 1
    else:
      prev_len = 0 if (num & 2) == 0 else curr_len
      curr_len = 0
    max_len = max(max_len, curr_len + prev_len + 1)
    num = num >> 1

  return max_len


[(to_bin(num), flip_bit_to_win(num)) for num in range(10)]

flip_bit_to_win(1775)
flip_bit_to_win(495587)
