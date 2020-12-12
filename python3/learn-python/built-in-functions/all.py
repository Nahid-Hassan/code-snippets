"""
    all(iterable): The all() method returns True when all elements in the given iterable are true. If not, it returns False.

    iterable:
        list, dict, string

    | When	                                | Return Value
    | --------------------------------------|-------------
    | All values are true 	                | True
    | All values are false	                | False
    | One value is true (others are false)	| False
    | One value is false (others are true)	| False
    | Empty Iterable	                    | True

"""

# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))


s = "This is good"
print(all(s))

# 0 is False
# '0' is True
s = '000'
print(all(s))

s = ''
print(all(s))


s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))
