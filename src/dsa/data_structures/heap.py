# from dsa.misc.class_generator import add_property, generate_class

# generate_class('Heap', 'src/dsa/data_structures/heap.py')
# add_property('Heap', 'src/dsa/data_structures/heap.py', 'heap_size')
# add_property('Heap', 'src/dsa/data_structures/heap.py', 'heap')

# generate_class('MaxHeap', 'src/dsa/data_structures/heap.py')
# generate_class('MinHeap', 'src/dsa/data_structures/heap.py')

from abc import ABC, abstractmethod


class Heap(ABC):
  """The Heap class"""
  def __init__(self, mylist=None):
    if mylist is None:
      mylist = []
    self._heap_size = len(mylist)
    self._heap = mylist
    for key in range(int(self._heap_size / 2) - 1, -1, -1):
      self.heapify(self._heap, key)

  @property
  def heap_size(self):
    return self._heap_size

  @property
  @abstractmethod
  def sign(self):
    pass

  def parent(self, key):
    return int((key - 1) / 2)

  def left(self, key):
    return 2 * key + 1

  def right(self, key):
    return 2 * key + 2

  def heapify(self, mylist, key):
    left = self.left(key)
    right = self.right(key)
    sign = self.sign
    if left < len(mylist) and sign * mylist[left] > sign * mylist[key]:
      tmp = left
    else:
      tmp = key
    if right < len(mylist) and sign * mylist[right] > sign * mylist[tmp]:
      tmp = right
    if tmp != key:
      mylist[tmp], mylist[key] = mylist[key], mylist[tmp]
      self.heapify(mylist, tmp)

  def peek(self):
    if self.heap_size == 0:
      raise IndexError('Heap underflow')
    else:
      return self[0]

  def pop(self):
    heap_size = self.heap_size
    if heap_size == 0:
      raise IndexError('Heap underflow')
    else:
      tmp = self[0]
      self[0] = self[heap_size - 1]
      del self[heap_size - 1]
      self._heap_size -= 1
      self.heapify(self, 0)
      return tmp

  def update_value(self, key, value):
    sign = self.sign
    if sign * value > sign * self[key]:
      tmp = 'smaller' if sign == 1 else 'bigger'
      raise ValueError('New value is {} than current value'.format(tmp))
    self[key] = value
    parent = self.parent(key)
    while key > 0 and sign * self[parent] < sign * self[key]:
      heap[parent], heap[key] = heap[key], heap[parent]
      key = parent
      parent = self.parent(key)

  def insert(self, value):
    self._heap_size += 1
    self._heap.append(self.sign * float('inf'))
    self.update_value(self._heap_size - 1, value)

  def __getitem__(self, key):
    return self._heap.__getitem__(key)

  def __setitem__(self, key, value):
    self._heap.__setitem__(key, value)

  def __delitem__(self, key):
    self._heap.__delitem__(key)

  def __len__(self):
    return self.heap_size

  def __str__(self):
    return str(self._heap)


class MaxHeap(Heap):
  @property
  def sign(self):
    return 1


class MinHeap(Heap):
  @property
  def sign(self):
    return -1


def heapsort(mylist, asc=True):
  heap = MaxHeap(mylist) if asc else MinHeap(mylist)
  for key in range(len(heap) - 1, 0, -1):
    tmp = heap[key]
    heap[key] = heap[0]
    heap[0] = tmp
    heap._heap_size -= 1
    heap.heapify(heap, 0)


if __name__ == '__main__':

  from icecream import ic
  for heap_type in [MaxHeap, MinHeap]:
    ic(heap_type)
    aa = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    ic(aa)
    heap = heap_type(aa)
    ic(heap.__str__())
    ic(heap.pop())
    ic(heap.__str__())
    ic(heap.insert(7.5))
    ic(heap.insert(2.5))
    ic(heap.__str__())

    aa = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    if 'Max' in str(heap_type):
      ic(heapsort(aa, asc=True))
    else:
      ic(heapsort(aa, asc=False))
    ic(aa)
    ic('----------')
