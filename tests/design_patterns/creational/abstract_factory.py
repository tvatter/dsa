# https://python-patterns.guide/gang-of-four/abstract-factory/
# not useful because callable are first-class citizens in Python
# and even if it werern't, classes are via @static_method

from decimal import Decimal

# In Python: a factory function.


def build_decimal(string):
  return Decimal(string.lstrip('$'))


# In some legacy languages: the code must
# move inside a class method instead.


class DecimalFactory(object):
  @staticmethod
  def build(string):
    return Decimal(string.lstrip('$'))


class Loader(object):
  @staticmethod
  def load(string, factory):
    string = string.rstrip(',')  # allow trailing comma
    return [factory.build(item) for item in string.split(',')]


f = DecimalFactory()

result = Loader.load('464.80, 993.68', f)
print(result)

# Complete abstract factory...

from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
  @abstractmethod
  def build_sequence(self):
    pass

  @abstractmethod
  def build_number(self, string):
    pass


class Factory(AbstractFactory):
  def build_sequence(self):
    return []

  def build_number(self, string):
    return Decimal(string)


class Loader2(object):
  @staticmethod
  def load(string, factory):
    sequence = factory.build_sequence()
    for substring in string.split(','):
      item = factory.build_number(substring)
      sequence.append(item)
    return sequence


f = Factory()
result = Loader2.load('1.23, 4.56', f)
print(result)
