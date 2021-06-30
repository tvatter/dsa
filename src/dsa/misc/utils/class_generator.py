import re
from os import path


def preprocess_file(class_name='MyClass', file_name=None, property_name=None):
  if file_name is None:
    file_name = class_name.lower() + '.py'

  found = [False] * 3
  class_info = {
      'name': class_name,
      'definition': 'class {}:'.format(class_name)
  }

  if path.exists(file_name):
    found[0] = True
    file = open(file_name, 'r')
    file_str = file.read()
    file.close()

  if found[0] and class_info['definition'] in file_str:
    found[1] = True

  if found[0] and not found[1] and file_str != '':
    class_info['definition'] = '\n\n' + class_info['definition']

  if found[0] and found[1] and property_name is not None:
    class_info = extend_class_info(class_info, file_str)
    if 'self._{} ='.format(property_name) in class_info['class_str']:
      found[2] = True

  return file_name, found, class_info


def get_property_defaults(property_name='my_property'):

  self_property = 'self._{}'.format(property_name)

  init = """
    self._{0} = {0}\n""".format(property_name)

  getter = """
  @property
  def {}(self):
    return {}\n""".format(property_name, self_property)

  setter = """
  @{0}.setter
  def {0}(self, new_{0}):
    {1} = new_{0}\n""".format(property_name, self_property)

  deleter = """
  @{0}.deleter
  def {0}(self):
    del {1}\n""".format(property_name, self_property)

  return init, getter, setter, deleter


def extend_class_info(class_info, file_str):

  # Start and end locations (could be improved)
  class_info['start'] = file_str.find(class_info['definition'])
  class_start_locations = [
      x.start() for x in re.compile(r'class .*:').finditer(file_str)
  ]
  class_start_index = class_start_locations.index(class_info['start'])
  if class_start_index + 1 == len(class_start_locations):
    class_end_location = len(file_str)
  else:
    class_end_index = class_start_index + 1
    class_end_location = class_start_locations[class_end_index] - 2
  class_info['end'] = class_end_location

  # To facilitation the addition of the property
  class_info['file_str'] = file_str
  class_str = file_str[class_info['start']:class_info['end']]
  class_info['class_str'] = class_str

  return class_info
