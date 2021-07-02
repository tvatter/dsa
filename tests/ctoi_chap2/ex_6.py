from copy import deepcopy
from queue import LifoQueue, Queue

from dsa.data_structures import LinkedList


# Simply copy, inverse and check that the two lists are equal
def is_palindrome(ll: LinkedList):

  ll_rev = deepcopy(ll)
  ll_rev.reverse()
  curr = ll.head
  curr_rev = ll_rev.head
  while curr:
    if curr.key != curr_rev.key:
      return False
    curr = curr.next_node
    curr_rev = curr_rev.next_node

  return True

# Doing the inversiong and copy at the same time
# Checking only for half is enough
def is_palindrome2(ll: LinkedList):

  curr_node, n_items, fifo_queue = reverse(ll)
  count = 0
  while count < int(n_items / 2):
    if curr_node.key != fifo_queue.get():
      return False
    else:
      curr_node = curr_node.next_node
    count += 1

  return True

# Reverse the LinkedList and uses a FIFO queue 
# to for the copy
def reverse(ll: LinkedList):
  fifo_queue = Queue()
  prev_node = None
  curr_node = ll.head

  n_items = 0
  while curr_node:
    fifo_queue.put(curr_node.key)
    n_items += 1
    next_node = curr_node.next_node
    curr_node.next_node = prev_node
    prev_node = curr_node
    curr_node = next_node

  curr_node = prev_node
  return curr_node, n_items, fifo_queue

# Two runners technique
def is_palindrome3(ll: LinkedList):
  p1 = ll.head
  p2 = ll.head.next_node
  if p2 is None:
    return True
  
  lifo_queue = LifoQueue()
  
  count = 1
  while p2:
    lifo_queue.put(p1.key)
    p1 = p1.next_node
    p2 = p2.next_node
    count += 1
    if p2 is not None:
      count += 1
      p2 = p2.next_node

  if count % 2 == 1:
    p1 = p1.next_node

  while p1:
    if p1.key != lifo_queue.get():
      return False
    p1 = p1.next_node
  
  return True
    

def runners_move(p1, p2):
  p1 = p1.next_node
  p2 = p2.next_node
  if p2 is not None:
    p2 = p2.next_node


l = [[1, 2, 3], [1], [1, 2], [1, 2, 1], [1, 2, 2, 1]]
for x in l:
  print(l)
  ll = LinkedList(x)
  print(is_palindrome(ll))
  ll2 = deepcopy(ll)
  print(is_palindrome2(ll2))
  ll2 = deepcopy(ll)
  print(is_palindrome3(ll2))

l2 = [1] * int(1e5)
%timeit ll2 = LinkedList(l2)
%timeit ll2 = LinkedList(l2); is_palindrome2(ll2)
%timeit ll2 = LinkedList(l2); is_palindrome3(ll2)
