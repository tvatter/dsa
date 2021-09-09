def get_bit(num, bit):
  return (num & (1 << bit)) != 0


def set_bit(num, bit):
  return num | (1 << bit)


def clear_bit(num, bit):
  return num & ~(1 << bit)


def clear_bits(num, bit, from_msb=True):
  if from_msb:
    return num & ~(~0 << bit)
  else:
    return num & (~0 << (bit + 1))


# def update_bit(num, bit, is_one=True):
#   if is_one:
#     return set_bit(num, bit)
#   else:
#     return clear_bit(num, bit)


def update_bit(num, bit, value=1):
  mask = ~(1 << bit)
  return (num & mask) | (value << bit)


def add(a, b, bits=32):
  res, carry = a ^ b, (a & b) << 1
  mask = ~(~0 << bits)
  while (carry & mask) != 0:
    res, carry = res ^ carry, (res & carry) << 1
  return res & mask if carry > 0 else res


# def substract(a, b, bits=32):
#   return add(a, add(~b, 1, bits), bits)


def substract(a, b, bits=32):
  res, borrow = a ^ b, (~a & b) << 1
  mask = ~(~0 << bits)
  while (borrow & mask) != 0:
    res, borrow = res ^ borrow, (~res & borrow) << 1
  return res | ~mask if borrow > 0 else res


def to_bin(num):
  num, digit = divmod(num, 2)
  res = str(int(digit))
  while num > 0:
    num, digit = divmod(num, 2)
    res += str(digit)
  return res[::-1]


def is_power_of_two(num):
  return (num & (num - 1)) == 0
