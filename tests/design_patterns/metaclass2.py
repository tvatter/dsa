## https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/

## Restrictions with multiple metaclasses

# class Meta1(type):
#   pass

# class Meta2(type):
#   pass

# class Base1(metaclass=Meta1):
#   pass

# class Base2(metaclass=Meta2):
#   pass

# class Foobar(Base1, Base2):
#   pass

# class Meta(type):
#   pass

# class SubMeta(Meta):
#   pass


class Base1(metaclass=Meta):
  pass


class Base2(metaclass=SubMeta):
  pass


class Foobar(Base1, Base2):
  pass


type(Foobar)
