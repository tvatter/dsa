import re

from dsa.utils.class_generator import get_property_defaults, preprocess_file


def generate_class(class_name='MyClass', file_name=None):

  file_name, found, class_info = preprocess_file(class_name, file_name)

  if found[1]:
    print('{} found in {}, exiting'.format(class_name, file_name))
  else:
    if found[0]:
      print('{} found, appending {}'.format(file_name, class_name))

    file = open(file_name, 'a')
    file.write(class_info['definition'] +
               '\n  """The {} class"""'.format(class_name) +
               '\n  def __init__(self):\n    pass\n')
    file.close()


def add_property(class_name='MyClass',
                 file_name=None,
                 property_name='my_property'):

  file_name, found, class_info = preprocess_file(class_name, file_name,
                                                 property_name)

  if not found[1]:
    print('{} not found in {}, exiting'.format(class_name, file_name))
  elif found[2]:
    print('{} found in {}, exiting'.format(property_name, class_name))
  else:
    init, getter, setter, deleter = get_property_defaults(property_name)
    file_str = class_info['file_str']
    class_str = class_info['class_str']
    init_regex = re.compile(r'(__init__\(self.*)\):')
    new_class_str = init_regex.sub(r'\1, {}=None):'.format(property_name),
                                   class_str)
    if '\n    pass' in new_class_str:
      new_class_str = new_class_str.replace('\n    pass\n', init)
    else:
      init_ind = new_class_str.find("\n\n")
      new_class_str = new_class_str[:init_ind] + init + new_class_str[
          init_ind + 1:]
    new_class_str = new_class_str + getter + setter + deleter
    file_str = file_str.replace(class_str, new_class_str)
    file = open(file_name, 'w')
    file.write(file_str)
    file.close()


if __name__ == '__main__':

  generate_class()
  add_property()
  add_property(property_name='another')

  generate_class('MyClass2', 'myclass.py')
  add_property('MyClass2', 'myclass.py')
  add_property('MyClass2', 'myclass.py', property_name='another')

  add_property(property_name='another2')
  add_property('MyClass2', 'myclass.py', property_name='another2')
