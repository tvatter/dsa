from typing import List


def robot_dfs(grid: List[List[bool]]):

  rows = len(grid)
  cols = len(grid[0])
  visited = [[False] * cols for _ in range(rows)]

  def dfs(row, col):

    if row == rows - 1 and col == cols - 1:
      return [(row, col)]

    # Try down
    new_pos = None
    if row + 1 < rows and grid[row + 1][col] and not visited[row + 1][col]:
      new_pos = dfs(row + 1, col)
      if new_pos:
        new_pos.append((row, col))
        return new_pos

    # Try right
    if col + 1 < cols and grid[row][col + 1] and not visited[row][col + 1]:
      new_pos = dfs(row, col + 1)
      if new_pos:
        new_pos.append((row, col))
        return new_pos

    return new_pos

  out = dfs(0, 0)
  out.reverse()
  return out


def robot_recurs(grid: List[List[bool]]):
  rows = len(grid)
  cols = len(grid[0])
  path = []

  def get_path(row, col):
    if row < 0 or col < 0 or (not grid[row][col]):
      return False

    if (row == 0 and col == 0) or get_path(row - 1, col) or get_path(
        row, col - 1):
      path.append((row, col))
      return True

    return False

  if get_path(rows - 1, cols - 1):
    return path
  else:
    return None


def robot_dp(grid: List[List[bool]]):
  rows = len(grid)
  cols = len(grid[0])
  no_path = set()
  path = []

  def get_path(row, col):
    if row < 0 or col < 0 or (not grid[row][col]):
      return False

    if (row, col) in no_path:
      return False

    if (row == 0 and col == 0) or get_path(row - 1, col) or get_path(
        row, col - 1):
      path.append((row, col))
      return True

    no_path.add((row, col))
    return False

  if get_path(rows - 1, cols - 1):
    return path
  else:
    return None

rows = 10
cols = 10
test0 = [[True] * cols for _ in range(rows)]
test1 = test0.copy()
test1.extend([[False] * cols])
test1[rows][cols - 1] = True
test2 = [[False] * cols for _ in range(rows)]
test3 = [[False] * cols for _ in range(rows)]
for i in range(rows):
  test2[i][i] = True
  test3[i][i] = True
  if i + 1 < cols:
    test2[i][i + 1] = True
    test3[i + 1][i] = True
test4 = [[False] * cols for _ in range(rows)]
for i in range(rows):
  for j in range(cols - i):
    test4[i][j] = True
  test4[i][cols - 1] = True

%timeit robot_dfs(test0)
%timeit robot_dfs(test1)
%timeit robot_dfs(test2)
%timeit robot_dfs(test3)
%timeit robot_dfs(test4)

%timeit robot_recurs(test0)
%timeit robot_recurs(test1)
%timeit robot_recurs(test2)
%timeit robot_recurs(test3)
%timeit robot_recurs(test4)

%timeit robot_dp(test0)
%timeit robot_dp(test1)
%timeit robot_dp(test2)
%timeit robot_dp(test3)
%timeit robot_dp(test4)
