# from dsa.misc.class_generator import add_property, generate_class

# generate_class('Stack', 'src/dsa/data_structures/stack.py')
# add_property('Stack', 'src/dsa/data_structures/stack.py', 'top')

from dsa.data_structures.node import Node


class Stack:
  """The Stack class"""
  def __init__(self):
    self._top = None

  @property
  def top(self):
    return self._top

  def isempty(self):
    return bool(self.top is None)

  def push(self, item):
    new_node = Node(data=item, prev_node=self.top)
    if self.top is not None:
      self._top.next_node = new_node
    self._top = new_node

  def extend(self, iterable):
    for item in iter(iterable):
      self.push(item)

  def pop(self):
    if self.isempty():
      raise IndexError('The stack is empty!')
    else:
      item = self._top.data
      self._top = self._top.prev_node
      return item

  def peek(self):
    if self.isempty():
      raise Exception('The stack is empty!')
    else:
      return self._top.data


# Alternative implementation using an list
class ArrayStack:
  def __init__(self, maxlen=10):
    self.n_items = 0
    self.maxlen = maxlen
    self.stack = [None] * maxlen

  def isempty(self):
    return bool(self.n_items == 0)

  def isfull(self):
    return bool(self.n_items == self.maxlen)

  def push(self, item):
    if self.isfull():
      raise IndexError('The stack is full')
    else:
      self.stack[self.n_items] = item
      self.n_items += 1

  def extend(self, iterable):
    for item in iter(iterable):
      self.push(item)

  def pop(self):
    if self.isempty():
      raise IndexError('The stack is empty')
    else:
      item = self.stack[self.n_items - 1]
      self.n_items -= 1
      self.stack[self.n_items] = None
      return item

  def peek(self):
    if self.isempty():
      raise IndexError('The stack is empty')
    else:
      return self.stack[self.n_items - 1]


# Array-based multi-stack
class MultiStack:
  def __init__(self, maxlen=10, nstacks=3):

    self.maxlen = maxlen
    self.nstacks = nstacks
    self.start = list(range(0, maxlen * nstacks, maxlen))
    self.n_items = [0] * nstacks
    self.stack = [None] * maxlen * nstacks

  def check_stackid(self, stackid):
    if stackid >= self.nstacks:
      raise IndexError('There are only {} stacks'.format(self.nstacks))

  def isempty(self, stackid):
    self.check_stackid(stackid)
    return bool(self.n_items[stackid] == 0)

  def isfull(self, stackid):
    self.check_stackid(stackid)
    return bool(self.n_items[stackid] == self.maxlen)

  def next_position(self, stackid):
    self.check_stackid(stackid)
    return self.start[stackid] + self.n_items[stackid]

  def push(self, item, stackid):
    if self.isfull(stackid):
      raise IndexError('The stack {} is full'.format(stackid))
    else:
      self.stack[self.next_position(stackid)] = item
      self.n_items[stackid] += 1

  def extend(self, iterable, stackid):
    for item in iter(iterable):
      self.push(item, stackid)

  def peek(self, stackid):
    if self.isempty(stackid):
      raise IndexError('The stack {} is empty'.format(stackid))
    else:
      curr_pos = self.next_position(stackid) - 1
      return self.stack[curr_pos]

  def pop(self, stackid):
    if self.isempty(stackid):
      raise IndexError('The stack {} is empty'.format(stackid))
    else:
      curr_pos = self.next_position(stackid) - 1
      item = self.stack[curr_pos]
      self.n_items[stackid] -= 1
      self.stack[curr_pos] = None
      return item


if __name__ == '__main__':

  from icecream import ic
  l = [1, 2, 3]

  for stack in [Stack(), ArrayStack()]:
    ic(stack)
    ic(stack.isempty())
    ic(stack.push(123))
    ic(stack.peek())

    ic(l)
    ic(stack.extend(l))
    ic(stack.peek())
    ic(stack.pop())
    ic(stack.peek())

  l = [1, 2, 3]
  stack = MultiStack(maxlen=3)
  ic(stack)
  ic(stack.stack)
  ic(l)
  ic(stack.extend(l, 0))
  ic(stack.extend(l, 1))
  ic(stack.extend(l, 2))
  ic(stack.stack)
  ic(stack.pop(0))
  ic(stack.pop(0))
  ic(stack.pop(1))
  ic(stack.peek(0))
  ic(stack.peek(1))
  ic(stack.stack)
