class Node:
  """The Node class"""
  def __init__(self, key=None, next_node=None, prev_node=None, data=None):
    self._key = key
    self._next_node = next_node
    self._prev_node = prev_node
    self._data = data

  @property
  def key(self):
    return self._key

  @key.setter
  def key(self, new_key):
    self._key = new_key

  @key.deleter
  def key(self):
    del self._key

  @property
  def next_node(self):
    return self._next_node

  @next_node.setter
  def next_node(self, new_next_node):
    self._next_node = new_next_node

  @next_node.deleter
  def next_node(self):
    del self._next_node

  @property
  def prev_node(self):
    return self._prev_node

  @prev_node.setter
  def prev_node(self, new_prev_node):
    self._prev_node = new_prev_node

  @prev_node.deleter
  def prev_node(self):
    del self._prev_node

  @property
  def data(self):
    return self._data

  @data.setter
  def data(self, new_data):
    self._data = new_data

  @data.deleter
  def data(self):
    del self._data
