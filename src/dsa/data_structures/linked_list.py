# from dsa.misc.class_generator import add_property, generate_class

# generate_class('LinkedList', 'src/dsa/data_structures/linked_list.py')
# add_property('LinkedList', 'src/dsa/data_structures/linked_list.py', 'head', setter=True)
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
    curr_node = self._head
    to_print = []
    while curr_node:
      to_print.append(str(curr_node.key))
      curr_node = curr_node.next_node

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
    curr_node = self._head
    while curr_node:
      if curr_node.key == key:
        return curr_node
      else:
        curr_node = curr_node.next_node

    return None

  def reverse(self):

    prev_node = None
    curr_node = self.head

    while curr_node:
      next_node = curr_node.next_node
      curr_node.next_node = prev_node
      if self.doubly:
        curr_node.prev_node = next_node

      prev_node = curr_node
      curr_node = next_node

    self.head = prev_node

  def delete_by_key(self, key):
    curr_node = self._head
    prev_node = None  # To handle both singly and doubly linked lists
    while curr_node:
      if curr_node.key == key:
        self.delete_by_ref(curr_node, prev_node)
        break
      prev_node = curr_node
      curr_node = curr_node.next_node

  def delete_by_ref(self, node, prev_node=None):
    next_node = node.next_node
    if prev_node is None and self.doubly:
      prev_node = node.prev_node

    if next_node is not None:
      node.key = next_node.key
      node.data = next_node.data
      node.next_node = next_node.next_node
      if self.doubly and next_node.next_node is not None:
        next_node.next_node.prev_node = node
    else:
      if self.doubly:
        if prev_node is None:
          self.head = None
        else:
          prev_node.next_node = None
      else:
        if prev_node is None:
          print(
              'Cannot delete the last node of a singly linked list by reference without the previous node'
          )
        else:
          prev_node.next_node = None

  def delete(self, key):
    # O(1) for if we have access to the node
    if isinstance(key, Node):
      self.delete_by_ref(key, key.prev_node)
    else:  # O(n) otherwise because it's basically a traversal
      self.delete_by_key(key)

  @property
  def head(self):
    return self._head

  @head.setter
  def head(self, new_head):
    self._head = new_head

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

  for doubly_test in [True, False]:
    ic('doubly linked: {}'.format(doubly_test))
    ll = LinkedList(l, doubly_test)
    ic(ll)
    ic(ll.__str__())

    ic(ll.reverse())
    ic(ll.__str__())

    ic(ll.delete(4))
    ic(ll.__str__())

    ic(ll.delete(3))
    ic(ll.__str__())

    ic(ll.delete(ll.head.next_node))
    ic(ll.__str__())

    ic(ll.delete(ll.head))
    ic(ll.__str__())

    ll2 = LinkedList(l2, doubly_test)
    ic(ll2)
    if doubly_test:
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
