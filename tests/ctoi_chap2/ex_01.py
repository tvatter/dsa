from dsa.data_structures import LinkedList
from icecream import ic


def remove_duplicates(my_ll: LinkedList):
  temp_dct = {}

  curr_node = my_ll.head
  prev_node = None
  while curr_node:
    next_node = curr_node.next_node
    key = curr_node.key
    if key not in temp_dct:
      temp_dct[key] = 0
      prev_node = curr_node
    else:
      prev_node.next_node = next_node
      if my_ll.doubly and next_node is not None:
        next_node.prev_node = prev_node

    curr_node = next_node


l = [1, 2, 3]
l2 = [1, 1, 2, 2, 3, 3]

for doubly_test in [True, False]:
  ic('doubly linked: {}'.format(doubly_test))
  ll = LinkedList(l, doubly_test)
  ic(str(ll))
  remove_duplicates(ll)
  ic(str(ll))

  l.reverse()
  ll = LinkedList(l, doubly_test)
  ic(str(ll))
  remove_duplicates(ll)
  ic(str(ll))

  ll2 = LinkedList(l2, doubly_test)
  ic(str(ll2))
  remove_duplicates(ll2)
  ic(str(ll2))

  l2.reverse()
  ll2 = LinkedList(l2, doubly_test)
  ic(str(ll2))
  remove_duplicates(ll2)
  ic(str(ll2))
