# from dsa.misc.class_generator import add_property, generate_class

# generate_class('LinkedList', 'src/dsa/data_structures/linked_list.py')
# add_property('LinkedList', 'src/dsa/data_structures/linked_list.py', 'head')
# add_property('LinkedList', 'src/dsa/data_structures/linked_list.py', 'doubly')

from dsa.data_structures.node import Node


class LinkedList:
  """The LinkedList class"""
  def __init__(self, array, doubly=True):
    self._head = None
    self._doubly = doubly
    for key in array:
      self.insert(key)

  def __str__(self):
    current_node = self._head
    to_print = []
    while current_node:
      to_print.append(str(current_node.key))
      current_node = current_node.next_node

    if self._doubly:
      return '<=>'.join(to_print)
    else:
      return '->'.join(to_print)

  def insert(self, key=None):
    new_node = Node(key, next_node=self._head)
    if self._head is not None and self._doubly:
      self._head.prev_node = new_node
    self._head = new_node

  def search(self, key):
    current_node = self._head
    while current_node:
      if current_node.key == key:
        return current_node
      else:
        current_node = current_node.next_node

    return None

  def delete_by_key(self, key):
    current_node = self._head
    prev_node = None  # To handle both singly and doubly linked lists
    while current_node:
      if current_node.key == key:
        self.delete_by_ref(current_node, prev_node)
        break
      prev_node = current_node
      current_node = current_node.next_node

  def delete_by_ref(self, current_node, prev_node):
    next_node = current_node.next_node
    if prev_node is None:
      self._head = next_node
      if self._doubly:
        self._head.prev_node = None
    else:
      prev_node.next_node = next_node
      if self._doubly:
        next_node.prev_node = prev_node

  def delete(self, key):
    # O(1) for doubly linked lists
    if isinstance(key, Node) and self._doubly:
      self.delete_by_ref(key, key.prev_node)
    else:  # O(n) otherwise because it's basically a search
      self.delete_by_key(key)

  @property
  def head(self):
    return self._head

  @property
  def doubly(self):
    return self._doubly


if __name__ == '__main__':

  from dsa.misc.timer import tic, toc
  from icecream import ic
  l = [1, 2, 3]
  ic(l)

  l2 = list(range(int(1e5)))
  ic(len(l2))

  for doubly in [True, False]:
    ic('doubly linked: {}'.format(doubly))
    ll = LinkedList(l, doubly)
    ic(ll)
    ic(ll.__str__())

    ic(ll.delete(4))
    ic(ll.__str__())

    ic(ll.delete(3))
    ic(ll.__str__())

    ll2 = LinkedList(l2, doubly)
    ic(ll2)
    if doubly:
      tic()
      ic('... worst case search')
      one_node = ll2.search(1)
      toc()
      ic('... worst case delete (by reference)')
      tic()
      ll2.delete(one_node)
      toc()
    else:
      ic('... worst case delete')
      tic()
      ll2.delete(1)
      toc()
    ic('..........................')
