from typing import List

from icecream import ic
from numpy import array
from numpy.random import PCG64, Generator

Vector = List[float]
Matrix = List[Vector]


def zero_matrix(mat: Matrix) -> None:

  m = len(mat)
  n = len(mat[0])

  zero_row = [False for _ in range(m)]
  zero_col = [False for _ in range(n)]
  for i in range(m):
    for j in range(n):
      if mat[i][j] == 0:
        zero_row[i] = True
        zero_col[j] = True

  for i in range(m):
    if zero_row[i]:
      nullify_row(mat, i)

  for i in range(n):
    if zero_col[i]:
      nullify_col(mat, i)


def nullify_row(mat: Matrix, row: int) -> None:

  n = len(mat[0])
  for j in range(n):
    mat[row][j] = 0


def nullify_col(mat: Matrix, col: int) -> None:

  n = len(mat)
  for j in range(n):
    mat[j][col] = 0


if __name__ == '__main__':

  rng = Generator(PCG64(12345))
  for _ in range(3):
    mat = rng.integers(0, 5, size=[4, 5], endpoint=True)
    ic(mat)
    zero_matrix(mat)
    ic(mat)
