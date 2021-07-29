from math import ceil, floor
from typing import List


def swap(nums, i, j):
  nums[i], nums[j] = nums[j], nums[i]


def partition(nums, l, r, x):
  for i in range(l, r):
    if nums[i] == x:
      swap(nums, r, i)
      break

  x = nums[r]
  i = l
  for j in range(l, r):
    if nums[j] <= x:
      swap(nums, i, j)
      i += 1
  swap(nums, i, r)
  return i


def find_median(nums, l, n):  # O(nlogn) but only used for n = 5
  tmp = []
  for i in range(l, l + n):
    tmp.append(nums[i])
  tmp.sort()
  return tmp[n // 2]


def select(nums: List[int], k: int = 1):
  if k > len(nums) or k < 1:
    raise ValueError('k should be in [1, len(nums)]')

  def select_aux(nums, l, r, k):
    n = r - l + 1
    if r == l:
      return nums[l]

    median = []
    j = 0
    for j in range(ceil(n / 5)):
      l_j = l + j * 5
      n_j = min(5, r - l_j + 1)
      median.append(find_median(nums, l_j, n_j))

    if j == 0:
      med_of_med = median[0]
    else:
      med_of_med = select_aux(median, 0, j, j // 2)

    pos = partition(nums, l, r, med_of_med)
    if pos - l == k - 1:
      return nums[pos]
    elif pos - l > k - 1:
      return select_aux(nums, l, pos - 1, k)
    else:
      return select_aux(nums, pos + 1, r, k - pos + l - 1)

  return select_aux(nums, 0, len(nums) - 1, k)


for j in range(1, 9):
  nums_test = [2, 8, 7, 1, 3, 5, 6, 4]
  print([j, select(nums_test, j)])
