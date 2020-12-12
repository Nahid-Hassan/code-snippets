"""
    bool(value): The bool() method converts a value to Boolean (True or False) using the standard truth testing procedure.

    value --> optional:
        It's not mandatory to pass a value to bool(). If you do not pass a value, bool() returns False.
        In general use, bool() takes a single parameter value.

    All false(Considered) values in Python,
        * None, false, 0, 0.0, 0j, (), [], {}, ''
        * objects of Classes which has __bool__() or __len()__ method which returns 0 or False
"""

test = []
print(test, 'is', bool(test))

test = [0]
print(test, 'is', bool(test))

test = 0.0
print(test, 'is', bool(test))

test = None
print(test, 'is', bool(test))

test = True
print(test, 'is', bool(test))

test = 'Easy string'
print(test, 'is', bool(test))


class String:
    str_obj = '0814341'

    def __index__(self):
        return int(self.str_obj)

    def __bool__(self):
        return bool(None)

s = String()
print(s)
print(bool(s))