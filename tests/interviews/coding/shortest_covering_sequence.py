  """
    Given a list of words, and a set of words,
    return the indices of the shortest subsequence of the list
    covering the set of words.

    >>> shortest_covering_sequence(['a', 'b', 'c', 'd', 'e'],
    ...                            {'a', 'b', 'c', 'd', 'e'}) == [0, 4]
    True
    >>> shortest_covering_sequence(['a', 'b', 'c', 'd', 'e'],
    ...                            {'a', 'b', 'c'}) == [0, 2]
    True
    >>> shortest_covering_sequence(['a', 'b', 'c', 'd', 'e'],
    ...                            {'a', 'b', 'd'}) == [0, 3]
    True
    >>> shortest_covering_sequence(['a', 'b', 'c', 'a', 'e'],
    ...                            {'a', 'b'}) == [0, 1]
    True
    >>> shortest_covering_sequence(['a', 'b', 'c', 'a', 'e'],
    ...                            {'a', 'c'}) == [2, 3]
    True
  """

from typing import List, Set

# def shortest_covering_sequence(list_of_words: List[str],
#                                set_of_words: Set[str]) -> List[int, int]:

#   if set_of_words.issubset(set(list_of_words)) is False:
#     return []

#   n = len(list_of_words)
#   curr = [0, n - 1]
#   for i in range(n):
#     for j in range(i, n):
#       if set(list_of_words[i:j + 1]) == set_of_words:
#         if j - i < curr[1] - curr[0]:
#           curr = [i, j]
#   return curr

def init_right(list_of_words, counter_of_words):
  right = -1
  found = set()

  while found is not counter_of_words.keys():
    
    right += 1
    word = list_of_words[right]

    if word not in counter_of_words.keys():
      continue

    counter_of_words[word] += 1
    found.add(word)

  return right

def shortest_covering_sequence(list_of_words: List[str],
                               set_of_words: Set[str]) -> List[int, int]:

  if set_of_words.issubset(set(list_of_words)) is False:
    return []

  counter = {word: 0 for word in set_of_words}

  right = init_right(list_of_words, counter)
  n = len(list_of_words)
  curr = [0, n - 1]
  while right < n:
    left = move_left(left, list_of_words, counter)
    if right - left < curr[1] - curr[0]:
      curr = [left, right]
    right = move_right(right, list_of_words, counter)
  return curr
