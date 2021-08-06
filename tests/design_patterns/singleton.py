class Singleton(type):
  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      print('Registering the class %s' % cls)
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
    return cls._instances[cls]
    # else: ## if you want to run __init__ every time the class is called, add
    #   cls._instances[cls].__init__(*args, **kwargs)


class MySingleton(metaclass=Singleton):
  def __init__(self):
    print('There can be only one!')
    self.state = 0


x = MySingleton()
y = MySingleton()
x == y
y.state = 1
x.state
