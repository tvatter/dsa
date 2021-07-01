# from dsa.misc.class_generator import add_property, generate_class

# generate_class('Node', 'src/dsa/data_structures/node.py')
# add_property('Node', 'src/dsa/data_structures/node.py', 'key')
# add_property('Node',
#              'src/dsa/data_structures/node.py',
#              'next_node',
#              setter=True)
# add_property('Node',
#              'src/dsa/data_structures/node.py',
#              'prev_node',
#              setter=True)
# add_property('Node', 'src/dsa/data_structures/node.py', 'data', setter=True)


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
