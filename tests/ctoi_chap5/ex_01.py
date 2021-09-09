def update_bit(num, bit, value):
  mask = ~(1 << bit)
  return (num & mask) | (value << bit)


def get_bit(num, bit):
  return (num & (1 << bit)) != 0


def insert_bits(n, m, i, j):
  for bit in range(i, j + 1):
    n = update_bit(n, bit, get_bit(m, bit - i))
  return n


def insert_bits_mask(n, m, i, j):
  mask = (~0 << (j + 1)) + ~(~0 << i)
  n = n & mask
  m = m << i
  return n | m


n = 2**11
m = 0b10011
i = 2
j = 6
bin(insert_bits(n, m, 2, 6))
bin(insert_bits_mask(n, m, 2, 6))
