# from dsa.misc.class_generator import add_property, generate_class

# generate_class('Heap', 'src/dsa/data_structures/heap.py')
# add_property('Heap', 'src/dsa/data_structures/heap.py', 'heap_size')
# add_property('Heap', 'src/dsa/data_structures/heap.py', 'heap')

# generate_class('MaxHeap', 'src/dsa/data_structures/heap.py')
# generate_class('MinHeap', 'src/dsa/data_structures/heap.py')

from abc import ABC, abstractmethod


class Heap(ABC):
  """The Heap class"""
  def __init__(self, values=None, handles=None):
    if values is None:
      values = []
    self._heap_size = len(values)
    self._values = values
    if handles is not None and len(handles) != len(values):
      raise ValueError('Handles should have the same size as the values')
    self._handles = handles
    if self._handles is not None:
      self._keys = {
          handle: key
          for handle, key in zip(handles, range(len(values)))
      }
    else:
      self._keys = None
    for key in range(int(self._heap_size / 2) - 1, -1, -1):
      self.heapify(key)

  @property
  def heap_size(self):
    return self._heap_size

  @property
  def values(self):
    return self._values

  @property
  def keys(self):
    return self._keys

  @property
  def handles(self):
    return self._handles

  @abstractmethod
  def compare(self, left, right):
    pass

  @property
  @abstractmethod
  def default_value(self):
    pass

  def parent(self, key):
    return int((key - 1) / 2)

  def left(self, key):
    return 2 * key + 1

  def right(self, key):
    return 2 * key + 2

  def isempty(self):
    return bool(self._heap_size == 0)

  def _swap(self, key1, key2):
    self._values[key1], self._values[key2] = self._values[key2], self._values[
        key1]
    if self._handles is not None:
      self._handles[key1], self._handles[key2] = self._handles[
          key2], self._handles[key1]
      self._update_keys(key1)
      self._update_keys(key2)

  def _update_keys(self, key):
    self._keys[self._handles[key]] = key

  def heapify(self, key):
    left = self.left(key)
    right = self.right(key)
    if left < self._heap_size and self.compare(self._values[left],
                                               self._values[key]):
      tmp = left
    else:
      tmp = key
    if right < self._heap_size and self.compare(self._values[right],
                                                self._values[tmp]):
      tmp = right
    if tmp != key:
      self._swap(key, tmp)
      self.heapify(tmp)

  def peek(self):
    if self._heap_size == 0:
      raise IndexError('Heap underflow')
    else:
      if self._handles is None:
        return self._values[0]
      else:
        return self._handles[0], self._values[0]

  def pop(self):
    heap_size = self._heap_size
    if heap_size == 0:
      raise IndexError('Heap underflow')
    else:
      value = self._values[0]
      self._values[0] = self._values[heap_size - 1]
      del self._values[heap_size - 1]
      if self._handles is not None:
        handle = self._handles[0]
        self._handles[0] = self._handles[heap_size - 1]
        self._update_keys(0)
        del self._handles[heap_size - 1]
      self._heap_size -= 1
      self.heapify(0)
      if self._handles is None:
        return value
      else:
        return handle, value

  def update_value(self, key, value):
    if not self.compare(value, self._values[key]):
      tmp = 'smaller' if self.default_value < 0 else 'bigger'
      raise ValueError('New value is {} than current value'.format(tmp))
    self._values[key] = value
    parent = self.parent(key)
    while key > 0 and not self.compare(self._values[parent],
                                       self._values[key]):
      self._swap(parent, key)
      key = parent
      parent = self.parent(key)

  def insert(self, value, handle=None):

    if self._handles is not None:
      handle = handle if handle is not None else self._heap_size
      self._handles.append(handle)
      self._keys[handle] = self._heap_size

    default_value = self.default_value
    if isinstance(value, list):
      default_value = [default_value] * len(value)
    self._values.append(default_value)

    self._heap_size += 1
    self.update_value(self._heap_size - 1, value)

  def __len__(self):
    return self._heap_size

  def __str__(self):
    if self._handles is None:
      return str(self._values)
    else:
      return str({
          handle: value
          for handle, value in zip(self._handles, self._values)
      })  # return str({
    #     handle: [value, self._keys[handle]]
    #     for handle, value in zip(self._handles, self._values)
    # })


class MaxHeap(Heap):
  def compare(self, left, right):
    return left > right

  @property
  def default_value(self):
    return -1 * float('inf')


class MinHeap(Heap):
  def compare(self, left, right):
    return left < right

  @property
  def default_value(self):
    return float('inf')


def heapsort(values, asc=True):
  heap = MaxHeap(values) if asc else MinHeap(values)
  for key in range(len(heap) - 1, 0, -1):
    tmp = heap.values[key]
    heap.values[key] = heap.values[0]
    heap.values[0] = tmp
    heap._heap_size -= 1
    heap.heapify(0)


if __name__ == '__main__':

  from icecream import ic
  for heap_type in [MaxHeap, MinHeap]:
    ic(heap_type)

    ic('.... without handles')
    values = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    ic(values)
    heap = heap_type(values)
    ic(heap.__str__())
    ic(heap.pop())
    ic(heap.__str__())
    ic(heap.insert(7.5))
    ic(heap.insert(2.5))
    ic(heap.__str__())

    ic('.... with handles')
    from string import ascii_lowercase
    ids = list(ascii_lowercase[:len(values) - 1])
    values = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    ic({a: b for a, b in zip(ids, values)})
    heap = heap_type(values, ids)
    ic(heap.__str__())
    ic(heap.pop())
    ic(heap.__str__())
    ic(heap.insert(7.5, 'foo'))
    ic(heap.__str__())
    ic(heap.insert(2.5, 'bar'))
    ic(heap.__str__())

    ic('..... sorting')
    values = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    if 'Max' in str(heap_type):
      ic(heapsort(values, asc=True))
    else:
      ic(heapsort(values, asc=False))
    ic(values)
    ic('----------')
