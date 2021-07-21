class Node:
  def __init__(self, key=None, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right


class Tree:
  def __init__(self, sorted_array):
    self.height, self.root = self.build_tree(sorted_array)

  def build_tree(self, sorted_array):
    n = len(sorted_array)
    if n == 0:
      return 0, None
    elif n == 1:
      return 1, Node(sorted_array[0])
    else:
      mid = int(n / 2)
      h_l, left = self.build_tree(sorted_array[:mid])
      h_r, right = self.build_tree(sorted_array[mid + 1:])
      return max(h_l, h_r) + 1, Node(sorted_array[mid], left, right)


sorted_array = list(range(7))
tree = Tree(sorted_array)

tree.root.key
tree.root.left.key
tree.root.left.left.key
tree.root.left.right.key
tree.root.right.key
tree.root.right.left.key
tree.root.right.right.key

n_max = 100
heights = []
from math import floor, log2

for j in range(1, n_max):
  sorted_array = list(range(j))
  tree = Tree(sorted_array)
  heights.append([j, tree.height, 1 + floor(log2(j))])
