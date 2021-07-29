from typing import List


def countingsort(nums: List[int]):
  n = len(nums)
  output = [None] * n
  table = [0] * n
  for j in range(n):
    table[nums[j]] += 1
  for j in range(1, n):
    table[j] = table[j] + table[j - 1]
  for j in range(n - 1, -1, -1):
    output[table[nums[j]] - 1] = nums[j]
    table[nums[j]] = table[nums[j]] - 1
  return output


def kthlargest(nums: List[int], k=0):
  max_element = max(nums)
  frequencies = [0] * (max_element + 1)
  for j in range(len(nums)):
    frequencies[nums[j]] += 1
  count = 0
  for j in range(max_element + 1):
    count += frequencies[j]
    if count > k:
      return j


nums_test = [2, 5, 3, 0, 2, 3, 0, 3]
print(countingsort(nums_test))
for j in range(len(nums_test)):
  print(kthlargest(nums_test,j))
