from abc import ABC, abstractmethod

from dsa.data_structures import Queue


class Animal(ABC):
  def __init__(self, age):
    self.age = age

  def isolder(self, animal):
    return bool(self.age < animal.age)

  def __str__(self):
    return 'I am a {} with ID={}'.format(self.species, self.age)

  @property
  @abstractmethod
  def species(self):
    pass


class Dog(Animal):
  @property
  def species(self):
    return 'dog'


class Cat(Animal):
  @property
  def species(self):
    return 'cat'


class Shelter:
  def __init__(self):
    self.dogs = Queue()
    self.cats = Queue()
    self.age = 0

  def enqueue(self, animal):
    if animal == 'dog':
      dog = Dog(self.age)
      self.dogs.enqueue(dog)
    else:
      cat = Cat(self.age)
      self.cats.enqueue(cat)

    self.age += 1

  def isempty(self):
    return self.dogs.isempty() and self.cats.isempty()

  def dequeue(self):
    if self.isempty():
      raise IndexError('The shelter is empty')
    elif self.dogs.isempty() and not self.cats.isempty():
      return self.dequeue_cat()
    elif self.cats.isempty() and not self.dogs.isempty():
      return self.dequeue_dog()
    else:
      if self.cats.peek().isolder(self.dogs.peek()):
        return self.dequeue_cat()
      else:
        return self.dequeue_dog()

  def dequeue_cat(self):
    if self.cats.isempty():
      raise IndexError('No more cats')
    else:
      return self.cats.dequeue()

  def dequeue_dog(self):
    if self.dogs.isempty():
      raise IndexError('No more dogs')
    else:
      return self.dogs.dequeue()


shelter = Shelter()
for animal in ['cat', 'cat', 'dog', 'cat', 'dog', 'dog']:
  shelter.enqueue(animal)
str(shelter.dequeue())
str(shelter.dequeue_dog())
str(shelter.dequeue_cat())
str(shelter.dequeue())
