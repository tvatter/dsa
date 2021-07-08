# from dsa.misc.class_generator import add_property, generate_class

# generate_class('TreeNode', 'src/dsa/data_structures/tree_node.py')
# add_property('TreeNode',
#              'src/dsa/data_structures/tree_node.py',
#              'key',
#              setter=True)
# add_property('TreeNode',
#              'src/dsa/data_structures/tree_node.py',
#              'children',
#              setter=True)
# add_property('TreeNode',
#              'src/dsa/data_structures/tree_node.py',
#              'data',
#              setter=True)

# generate_class('BinTreeNode', 'src/dsa/data_structures/tree_node.py')
# add_property('BinTreeNode',
#              'src/dsa/data_structures/tree_node.py',
#              'left',
#              setter=True)
# add_property('BinTreeNode',
#              'src/dsa/data_structures/tree_node.py',
#              'right',
#              setter=True)

# generate_class('TrieNode', 'src/dsa/data_structures/tree_node.py')
# add_property('TrieNode',
#              'src/dsa/data_structures/tree_node.py',
#              'is_word',
#              setter=True)


class TreeNode:
  """The TreeNode class"""
  def __init__(self, key=None, children=None, data=None):
    self._key = key
    self._children = children
    self._data = data

  @property
  def key(self):
    return self._key

  @key.setter
  def key(self, new_key):
    self._key = new_key

  @property
  def children(self):
    return self._children

  @children.setter
  def children(self, new_children):
    self._children = new_children

  @property
  def data(self):
    return self._data

  @data.setter
  def data(self, new_data):
    self._data = new_data

  def __str__(self):
    return str(self.key)


class BinTreeNode(TreeNode):
  """The BinTreeNode class"""
  def __init__(self, key=None, left=None, right=None, data=None):
    super().__init__(key, [left, right], data)

  @property
  def left(self):
    return self.children[0]

  @left.setter
  def left(self, new_left):
    self.children[0] = new_left

  @property
  def right(self):
    return self.children[1]

  @right.setter
  def right(self, new_right):
    self.children[1] = new_right


class TrieNode(TreeNode):
  """The TrieNode class"""
  def __init__(self, key='', children=None):
    if children is None:
      children = {}
    super().__init__(key, children)
    self._is_word = False

  @property
  def is_word(self):
    return self._is_word

  @is_word.setter
  def is_word(self, new_is_word):
    self._is_word = new_is_word
