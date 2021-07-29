from typing import List


def insertion_sort(nums: List[int]):
  for j in range(1, len(nums)):
    key = nums[j]
    i = j - 1
    while i >= 0 and nums[i] > key:
      nums[i + 1] = nums[i]
      i = i - 1
    nums[i + 1] = key


nums_test = [2, 8, 7, 1, 3, 5, 6, 4]
insertion_sort(nums_test)
print(nums_test)
