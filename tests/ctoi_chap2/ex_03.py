from dsa.data_structures import LinkedList, ListNode


def delete_middle_node(mid_node: ListNode):
  next_node = mid_node.next_node
  mid_node.key = next_node.key
  mid_node.data = next_node.data
  mid_node.next_node = next_node.next_node
  mid_node.prev_node = next_node.prev_node


l = [1, 2, 3]
ll = LinkedList(l, doubly=False)
mid_n = ll.head.next_node
delete_middle_node(mid_n)
str(ll)
