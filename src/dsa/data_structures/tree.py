# from dsa.misc.class_generator import add_property, generate_class

# generate_class('Tree', 'src/dsa/data_structures/tree.py')
# add_property('Tree', 'src/dsa/data_structures/tree.py', 'root', setter=True)

# generate_class('BinTree', 'src/dsa/data_structures/tree.py')
# add_property('BinTree', 'src/dsa/data_structures/tree.py', 'root', setter=True)

# generate_class('Trie', 'src/dsa/data_structures/tree.py')
# add_property('Trie', 'src/dsa/data_structures/tree.py', 'root', setter=True)

from dsa.data_structures.tree_node import BinTreeNode, TreeNode, TrieNode


class Tree:
  """The Tree class"""
  def __init__(self, root=None):
    self._root = root

  @property
  def root(self):
    return self._root

  @root.setter
  def root(self, new_root):
    self._root = new_root


class BinTree(Tree):
  """The BinTree class"""
  def in_order_traversal(self, node):
    while node is not None:
      self.in_order_traversal(node.left)
      print(node)
      self.in_order_traversal(node.right)

  def pre_order_traversal(self, node):
    while node is not None:
      print(node)
      self.pre_order_traversal(node.left)
      self.pre_order_traversal(node.right)

  def post_order_traversal(self, node):
    while node is not None:
      self.post_order_traversal(node.left)
      self.post_order_traversal(node.right)
      print(node)


class Trie:
  """The Trie class"""
  def __init__(self):
    self._root = TrieNode()

  @property
  def root(self):
    return self._root

  @root.setter
  def root(self, new_root):
    self._root = new_root

  def insert(self, word):
    curr_node = self._root
    for i, l in enumerate(word):
      if l not in curr_node.children:
        prefix = word[0:i + 1]
        curr_node.children[l] = TrieNode(key=prefix)
      curr_node = curr_node.children[l]
    curr_node.is_word = True

  def find(self, word):
    curr_node = self._root
    for l in word:
      if l not in curr_node.children:
        return None
      curr_node = curr_node.children[l]
    if curr_node.is_word:
      return curr_node

  def size(self, node=None):
    if node is None:
      node = self._root
    count = 1
    for l in node.children:
      count += self.size(node.children[l])
    return count

  def __starts_from(self, node, words=None):
    if words is None:
      words = []
    if node.is_word:
      words.append(node.key)
    for l in node.children:
      self.__starts_from(node.children[l], words)

  def starts_with(self, prefix):
    words = []
    curr_node = self._root
    for l in prefix:
      if l not in curr_node.children:
        return words
      curr_node = curr_node.children[l]

    self.__starts_from(curr_node, words)
    return words


if __name__ == '__main__':

  from icecream import ic
  words = []

  trie = Trie()
  trie.insert('apple')
  trie.insert('app')
  trie.insert('aposematic')
  trie.insert('appreciate')
  trie.insert('book')
  trie.insert('bad')
  trie.insert('bear')
  trie.insert('bat')
  ic(trie.starts_with('app'))
  ic(trie.size())
