from dsa.data_structures.graph_node import TrieNode

# from dsa.misc.class_generator import add_property, generate_class

# generate_class('Trie', 'src/dsa/data_structures/tree_graph.py')
# add_property('Trie', 'src/dsa/data_structures/tree_graph.py', 'root', setter=True)


class Trie:
  """The Trie class"""
  def __init__(self, root: TrieNode = None):
    if root is None:
      root = TrieNode()
    self._root = root

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


# _end = '_end_'

# def trie_make(*words):
#   root = dict()
#   for word in words:
#     trie_insert(root, word)
#   return root

# def trie_insert(root, word):
#   current_dict = root
#   for letter in word:
#     current_dict = current_dict.setdefault(letter, {})
#   current_dict[_end] = _end

# def trie_find(trie, word):
#   current_dict = trie
#   for letter in word:
#     if letter not in current_dict:
#       return False
#     current_dict = current_dict[letter]
#   return _end in current_dict

# trie_make('foo', 'bar', 'baz', 'barz')
# trie_find(trie_make('foo', 'bar', 'baz', 'barz'), 'baz')
# trie_find(trie_make('foo', 'bar', 'baz', 'barz'), 'barz')
# trie_find(trie_make('foo', 'bar', 'baz', 'barz'), 'barzz')
# trie_find(trie_make('foo', 'bar', 'baz', 'barz'), 'bart')
# trie_find(trie_make('foo', 'bar', 'baz', 'barz'), 'ba')

if __name__ == '__main__':

  from icecream import ic

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
