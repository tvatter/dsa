from typing import List


def quicksort(nums: List[int]):
  def swap(i, j):
    nums[i], nums[j] = nums[j], nums[i]

  def quicksort_aux(l, r):
    if l < r:
      q = partition(l, r)
      quicksort_aux(l, q - 1)
      quicksort_aux(q + 1, r)

  def partition(l, r):
    x = nums[r]
    i = l
    for j in range(l, r):
      if nums[j] <= x:
        swap(i, j)
        i += 1
    swap(i, r)
    return i

  quicksort_aux(0, len(nums) - 1)


nums_test = [2, 8, 7, 1, 3, 5, 6, 4]
quicksort(nums_test)
print(nums_test)
