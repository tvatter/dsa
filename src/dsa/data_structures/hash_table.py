# from dsa.misc.class_generator import add_property, generate_class

# generate_class('HashTable', 'src/dsa/data_structures/hash_table.py')
# add_property('HashTable', 'src/dsa/data_structures/hash_table.py', 'array')
# add_property('HashTable', 'src/dsa/data_structures/hash_table.py',
#              'load_factor')
# add_property('HashTable', 'src/dsa/data_structures/hash_table.py', 'n_entries')
# add_property('HashTable', 'src/dsa/data_structures/hash_table.py', 'n_buckets')
from math import ceil


class HashTable:
  """The HashTable class"""
  def __init__(self, array=None, load_factor=0.75):
    self._load_factor = load_factor
    self._n_buckets = ceil(2 * len(array) / load_factor)
    self.init_array(array)

  def init_array(self, array):
    self._n_entries = 0
    self._array = [[] for _ in range(self._n_buckets)]
    for key in array:
      self.insert(key)

  def get_index(self, key):
    hash_key = hash(key)
    return hash_key % self._n_buckets

  def search(self, key):
    index_key = self.get_index(key)
    return key in self._array[index_key]

  def insert(self, key):
    index_key = self.get_index(key)
    if key not in self._array[index_key]:
      if (self._n_entries + 1) / self._n_buckets > self._load_factor:
        self.resize()
      self._n_entries += 1
      self._array[index_key].append(key)

  def delete(self, key):
    index_key = self.get_index(key)
    if key in self._array[index_key]:
      self._n_entries -= 1
      self._array[index_key].remove(key)

  def resize(self):
    self._n_buckets = int(self._n_entries * 2)
    old_array = [item for sub in self._array for item in sub]
    self.init_array(old_array)

  @property
  def array(self):
    return self._array

  @property
  def load_factor(self):
    return self._load_factor

  @property
  def n_entries(self):
    return self._n_entries

  @property
  def n_buckets(self):
    return self._n_buckets


if __name__ == '__main__':

  from string import ascii_letters

  from icecream import ic
  l = ['hi', 'abc', 'aa', 'ab']
  ic(l)

  h = HashTable(l)
  ic(h)
  ic(h.array)

  ic('... insert stuff')
  for key in ['ss', 'qe', '234']:
    h.insert(key)
  ic(h.array)

  ic('... insert more stuff (trigger resize)')
  for key in ascii_letters:
    h.insert(key)
  ic(h.array)

  ic('... remove stuff')
  for key in ascii_letters:
    h.delete(key)
  ic(h.array)
  ic(h.search('hi'))
  ic(h.search('ss'))
