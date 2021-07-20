from dsa.data_structures.graph_node import BinaryNode
from dsa.data_structures.tree import Tree

# from dsa.misc.class_generator import add_property, generate_class

# generate_class('BinaryTree', 'src/dsa/data_structures/tree_graph.py')
# add_property('BinaryTree', 'src/dsa/data_structures/tree_graph.py', 'root', setter=True)


class BinaryTree(Tree):
  """The BinaryTree class"""
  def __init__(self, root: BinaryNode = None):
    super().__init__(root)

  def in_order_traversal(self, node: BinaryNode = None):
    if node is not None:
      self.in_order_traversal(node.left)
      print(node)
      self.in_order_traversal(node.right)

  def pre_order_traversal(self, node: BinaryNode = None):
    if node is not None:
      print(node)
      self.pre_order_traversal(node.left)
      self.pre_order_traversal(node.right)

  def post_order_traversal(self, node: BinaryNode = None):
    if node is not None:
      self.post_order_traversal(node.left)
      self.post_order_traversal(node.right)
      print(node)

  # def search(self, node=None, key=0):
  #   if node is None or node.key == key:
  #     return node
  #   if key < node.key:
  #     return self.search(node.left, key)
  #   else:
  #     return self.search(node.right, key)

  def search(self, node=None, key=0):
    while node is not None and node.key != key:
      if key < node.key:
        node = node.left
      else:
        node = node.right
    return node

  def min(self, root=None):
    if root is None:
      root = self.root
    node = root
    while node.left is not None:
      node = node.left
    return node

  def max(self, root=None):
    if root is None:
      root = self.root
    node = root
    while node.right is not None:
      node = node.right
    return node

  def successor(self, node):
    if node.right is not None:
      return self.min(node.right)
    next_node = node.parent
    while next_node is not None and node == next_node.right:
      node = next_node
      next_node = node.parent
    return next_node

  def predecessor(self, node):
    if node.left is not None:
      return self.max(node.left)
    next_node = node.parent
    while next_node is not None and node == next_node.left:
      node = next_node
      next_node = node.parent
    return next_node

  def insert(self, node):
    parent = None
    curr_node = self.root
    while curr_node is not None:
      parent = curr_node
      if node.key < curr_node.key:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right
    node.parent = parent
    if parent is None:
      self._root = node
    elif node.key < parent.key:
      parent.left = node
    else:
      parent.right = node


if __name__ == '__main__':

  import numpy as np
  from icecream import ic
  from numpy.random import default_rng

  rng = default_rng()
  keys = rng.choice(20, 10, False)

  tree = BinaryTree()
  for key in keys:
    node = BinaryNode(key)
    tree.insert(node)

  ic(keys)
  ic(tree)

  ic(tree.in_order_traversal(tree.root))
  ic(tree.post_order_traversal(tree.root))
  ic(tree.pre_order_traversal(tree.root))

  ic(tree.min().key)
  ic(tree.max().key)

  ic(tree.min(tree.root.right).key)
  ic(tree.max(tree.root.left).key)
