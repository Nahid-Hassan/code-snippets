"""
    The callable() method returns True if the object passed appears callable. If not, it returns False.
    
    callable(object):
       * It important to remember that, even if callable() is True, call to the object may still fail.
       * However, if callable() returns False, call to the object will certainly fail.
"""

x = 50
print(callable(x))

x = 'name'
print(callable(x))

def my_function():
    print('test')

y = my_function
print(callable(y))

# Here, the object x is not callable. And, the object y appears to be callable (but may not be callable).


# callable object

class Foo:
  def __call__(self):
    print('Print Something')


print(callable(Foo))

foo_object = Foo()
foo_object()

# Object Appears to be Callable but isn't callable.


class Foo:
  def printLine(self):
    print('Print Something')


print(callable(Foo))
foo_object = Foo()
foo_object() # but this object is not callable
