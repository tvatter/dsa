def xml_checker0(input):
  queue = []

  while input:
    i = input.find("<")
    j = input.find(">")
    if i == -1 and j == -1:
      break
    if (i == -1 and j > -1) or (j == -1 and i > -1) or (j == i + 1):
      return False
    flag = input[i + 1:j]
    if flag == '/':
      return False
    if flag[0] == '/':
      if len(queue) == 0:
        return False
      last_flag = queue.pop()
      if flag[1:] != last_flag:
        return False
    else:
      queue.append(flag)
    input = input[j + 1:]

  return len(queue) == 0


def xml_checker(input):
  queue = []
  start = 0
  while input:
    i = input.find("<", start)
    j = input.find(">", start)
    if i == -1 and j == -1:
      break
    if (i == -1 and j > -1) or (j == -1 and i > -1) or (j == i + 1):
      return False
    flag = input[i + 1:j]
    if flag == '/':
      return False
    if flag[0] == '/':
      if len(queue) == 0:
        return False
      last_flag = queue.pop()
      if flag[1:] != last_flag:
        return False
    else:
      queue.append(flag)
    start = j + 1

  return len(queue) == 0


inputs = [
    'text <a> text</a>', '<a>text<b>other text</b></a>',
    '<a>text<b>other text</a></b>', '<a>text</b>', '<', '>', 'test</b>', 'test'
    'text <a> text</a> somemore',
    '<a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a><a>text<b>other text</b></a>'
]

[xml_checker(input) for input in inputs]

%timeit [xml_checker0(input) for input in inputs]
%timeit [xml_checker(input) for input in inputs]
