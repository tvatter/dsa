from itertools import chain
from typing import List

from dsa.data_structures.graph_node import GraphNode

# from dsa.misc.class_generator import add_property, generate_class

# generate_class('Tree', 'src/dsa/data_structures/tree.py')
# add_property('Tree', 'src/dsa/data_structures/tree.py', 'root', setter=True)


class Tree:
  """The Tree class"""
  def __init__(self, root: GraphNode = None):
    self._root = root

  @property
  def root(self):
    return self._root

  @root.setter
  def root(self, new_root):
    self._root = new_root
