# from dsa.misc.class_generator import add_property, generate_class

# generate_class('ListNode', 'src/dsa/data_structures/list_node.py')
# add_property('ListNode',
#              'src/dsa/data_structures/list_node.py',
#              'key',
#              setter=True)
# add_property('ListNode',
#              'src/dsa/data_structures/list_node.py',
#              'next_node',
#              setter=True)
# add_property('ListNode',
#              'src/dsa/data_structures/list_node.py',
#              'prev_node',
#              setter=True)
# add_property('ListNode',
#              'src/dsa/data_structures/list_node.py',
#              'data',
#              setter=True)


class ListNode:
  """The ListNode class"""
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

  @property
  def next_node(self):
    return self._next_node

  @next_node.setter
  def next_node(self, new_next_node):
    self._next_node = new_next_node

  @property
  def prev_node(self):
    return self._prev_node

  @prev_node.setter
  def prev_node(self, new_prev_node):
    self._prev_node = new_prev_node

  @property
  def data(self):
    return self._data

  @data.setter
  def data(self, new_data):
    self._data = new_data

  def __str__(self):
    return str(self.key)
