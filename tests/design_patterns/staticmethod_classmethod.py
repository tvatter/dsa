# https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod


class A(object):
  def foo(self, x):
    print(f"executing foo({self}, {x})")

  @classmethod
  def class_foo(cls, x):
    print(f"executing class_foo({cls}, {x})")

  @staticmethod
  def static_foo(x):
    print(f"executing static_foo({x})")


a = A()
a.foo(1)
a.class_foo(1)
A.class_foo(1)
a.static_foo(1)
A.static_foo(1)

print(a.foo)
print(a.class_foo)
print(a.static_foo)
print(A.class_foo)
print(A.static_foo)
