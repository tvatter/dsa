from collections import deque


def sort_squared(nums):
  out = deque()
  left = 0
  right = len(nums) - 1
  while left <= right:
    if abs(nums[left]) > abs(nums[right]):
      out.appendleft(nums[left]**2)
      left += 1
    else:
      out.appendleft(nums[right]**2)
      right -= 1

  return out


sort_squared([-4, -1, 0, 3, 10])
sort_squared([-7, -3, 2, 3, 11])
