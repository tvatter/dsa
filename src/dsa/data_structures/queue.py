# from dsa.misc.class_generator import add_property, generate_class

# generate_class('Queue', 'src/dsa/data_structures/queue.py')
# add_property('Queue', 'src/dsa/data_structures/queue.py', 'head')
# add_property('Queue', 'src/dsa/data_structures/queue.py', 'tail')

from dsa.data_structures.node import Node


class Queue:
  """The Queue class"""
  def __init__(self):
    self._head = None
    self._tail = None

  @property
  def head(self):
    return self._head

  @property
  def tail(self):
    return self._tail

  def isempty(self):
    return bool(self.head is None)

  def enqueue(self, item):
    new_node = Node(data=item, next_node=self._tail)
    if self.isempty():
      self._head = new_node
      self._tail = new_node
    else:
      self._tail.prev_node = new_node
      self._tail = new_node

  def extend(self, iterable):
    for item in iter(iterable):
      self.enqueue(item)

  def dequeue(self):
    if self.isempty():
      raise IndexError('The queue is empty!')
    else:
      item = self._head.data
      self._head = self._head.prev_node
      return item

  def peek(self):
    if self.isempty():
      raise Exception('The queue is empty!')
    else:
      return self._head.data


if __name__ == '__main__':

  from icecream import ic
  l = [1, 2, 3]

  queue = Queue()
  ic(queue)
  ic(queue.isempty())
  ic(queue.enqueue(123))
  ic(queue.peek())

  ic(l)
  ic(queue.extend(l))
  ic(queue.peek())
  ic(queue.dequeue())
  ic(queue.peek())
