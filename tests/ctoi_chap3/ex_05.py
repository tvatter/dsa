from dsa.data_structures import ArrayStack

Stack = ArrayStack


def sort_stack(stack):

  tmp_stack = Stack(maxlen=stack.maxlen)
  while not stack.isempty():
    tmp_item = stack.pop()
    while not tmp_stack.isempty() and tmp_stack.peek() < tmp_item:
      stack.push(tmp_stack.pop())
    tmp_stack.push(tmp_item)

  return tmp_stack

# Alternative using a recursion (slower !!!)
# def merge_item(stack, item):

#   if stack.isempty() or item <= stack.peek():
#     stack.push(item)
#   else:
#     curr_item = stack.pop()
#     merge_item(stack, item)
#     stack.push(curr_item)


# def sort_stack(stack):
#   if stack.isempty():
#     return stack
#   else:
#     curr_item = stack.pop()
#     temp_stack = sort_stack(stack)
#     merge_item(temp_stack, curr_item)
#     return temp_stack


l = [[1, 2, 3], [1], [1, 2], [4, 2, 1], [1, 2, 2, 1], [4, 5, 1, 2],
     [4, 5, 1, 3, 2],
     list(range(11))]
for ll in l:
  stack = Stack(maxlen=len(ll)); stack.extend(ll); sorted_stack = sort_stack(stack)
  print([ll, sorted_stack.stack[0:len(ll)]])

maxlen = int(1e3)
ll = list(range(maxlen))
%timeit stack = Stack(maxlen=maxlen); stack.extend(ll)
%timeit stack = Stack(maxlen=maxlen); stack.extend(ll); sorted_stack = sort_stack(stack)

