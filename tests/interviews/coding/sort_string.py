# Write a function that takes in a string containing words and
# numbers separated by spaces and returns a new string
# containing the same words and number, but that respects three
# (3) properties: (a) numbers are sorted numerically; (b) words
# are sorted alphabetically; (c) if the k th input token is a word
# (number), the k th output token must be a word (number).


def sort_string(s):
  s = s.split(',')
  numbers = []
  words = []
  is_number = []
  for x in s:
    if x[0].isdigit():
      numbers.append(int(x))
      is_number.append(True)
    else:
      words.append(x)
      is_number.append(False)

  numbers.sort(reverse=True)
  words.sort(reverse=True)

  out = []
  for val in is_number:
    if val:
      out.append(str(numbers.pop()))
    else:
      out.append(words.pop())

  return ','.join(out)


sort_string('456,a,c,12,b,4')
