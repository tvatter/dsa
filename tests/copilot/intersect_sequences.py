'''
 |--|       |---------| GOLD
   |--| |-|      |---|  PRED
   ||            |---|  INTERSECT
'''

from typing import List


def intersect_intervals(i1: List[int, int], i2: List[int,
                                                     int]) -> List[int, int]:
  '''
     Find the intersection of two intervals.
  '''
  if i1[1] < i2[0] or i2[1] < i1[0]:
    return []
  return [max(i1[0], i2[0]), min(i1[1], i2[1])]


def intersect_sequences(seq1: List[List[int, int]],
                        seq2: List[List[int, int]]) -> List[List[int, int]]:
  '''
     Find the intersection of two sequences of intervals.
  '''
  if len(seq1) == 0 or len(seq2) == 0:
    return []
  result = []
  i1 = 0
  i2 = 0
  while i1 < len(seq1) and i2 < len(seq2):
    inter = intersect_intervals(seq1[i1], seq2[i2])
    if len(inter) > 0:
      result.append(inter)
    if seq1[i1][1] < seq2[i2][1]:
      i1 += 1
    elif seq2[i2][1] < seq1[i1][1]:
      i2 += 1
    else:
      i1 += 1
      i2 += 1
  return result
