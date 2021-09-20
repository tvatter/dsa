def gcd_naive(x, y):
  out = 1
  for i in range(2, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
      out = i

  return out


def gcd_euclid_recurs(x, y):
  x, y = max(x, y), min(x, y)
  if y:
    return gcd_euclid_recurs(y, x % y)
  else:
    return x


def gcd_euclid_iter(x, y):
  x, y = max(x, y), min(x, y)
  while y:
    x, y = y, x % y
  return x


def gcd_bin_recurs(x, y):
  if x == y:
    return int(x)
  else:
    x_even = x % 2 == 0
    y_even = y % 2 == 0
    if x_even and y_even:
      return 2 * gcd_bin_recurs(x / 2, y / 2)
    elif x_even and not y_even:
      return gcd_bin_recurs(x / 2, y)
    elif y_even and not x_even:
      return gcd_bin_recurs(x, y / 2)
    else:
      x, y = max(x, y), min(x, y)
      return gcd_bin_recurs(y, (x - y) / 2)


def gcd_bin_iter(x, y):
  shift = 0
  while x != y:
    x_even = x % 2 == 0
    y_even = y % 2 == 0
    if x_even and y_even:
      shift += 1
      x, y = x >> 1, y >> 1
    elif x_even and not y_even:
      x >>= 1
    elif y_even and not x_even:
      y >>= 1
    else:
      x, y = min(x, y), (max(x, y) - min(x, y)) >> 1
  return int(x) << shift


def trailing_zeros(num):
  return 0 if num == 0 else (num & -num).bit_length() - 1


def gcd_bin_iter_improve(x, y):
  shift = trailing_zeros(x | y)
  x >>= trailing_zeros(x)
  while y:
    y >>= trailing_zeros(y)
    if x > y:
      x, y = y, x
    y = y - x
  return x << shift


# %timeit gcd_naive(48, 18)
# %timeit gcd_euclid_recurs(48, 18)
# %timeit gcd_euclid_iter(48, 18)
# %timeit gcd_bin_recurs(48, 18)
# %timeit gcd_bin_iter(48, 18)
# %timeit gcd_bin_iter_improve(48, 18)


def is_prime_naive(n):
  if n < 2:
    return False
  else:
    for i in range(2, n):
      if n % i == 0:
        return False
    return True


def is_prime_better(n):
  if n < 2:
    return False
  else:
    for i in range(2, int(n**1 / 2)):
      if n % i == 0:
        return False
    return True


# %timeit is_prime_naive(7919)
# %timeit is_prime_better(7919)

# def sieve_of_eratosthenes(num):

#   out = []
#   if num < 2:
#     return out

#   flags = [True] * (num + 1)
#   flags[0], flags[1] = False, False

#   prime = 2
#   while prime <= int(num ** (1/2)):
#     out.append(prime)
#     flags[prime ** 2::prime] = [False] * len(flags[prime ** 2::prime])
#     prime = prime + 1 + flags[prime + 1::].index(True)

#   while prime <= num:
#     out.append(prime)
#     try:
#       prime = prime + 1 + flags[prime + 1::].index(True)
#     except:
#       break

#   return out

# len(sieve_of_eratosthenes(7919)) == 1000


def sieve_of_eratosthenes(num):

  flags = [True] * (num + 1)
  flags[0], flags[1] = False, False

  prime = 2
  while prime <= int(num**(1 / 2)):
    flags[prime**2::prime] = [False] * len(flags[prime**2::prime])
    prime = prime + 1 + flags[prime + 1::].index(True)

  return flags


# len([x for x in sieve_of_eratosthenes(7919) if x == True]) == 1000


def is_prime_eratosthenes(num):
  primes = sieve_of_eratosthenes(num)
  return primes[-1] is True


# %timeit is_prime_naive(7919)
# %timeit is_prime_better(7919)
# %timeit is_prime_eratosthenes(7919)
