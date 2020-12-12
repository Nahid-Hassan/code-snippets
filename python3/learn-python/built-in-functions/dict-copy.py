"""
    They copy() method returns a shallow copy of the dictionary.
    
    dict.copy():
        copy() method doesn't take any parameters.
"""
original = {1: 'one', 2: 'two'}
new = original.copy()

print('Original: ', original)
print('New: ', new)


# difference between 'copy' and '='
# copy
original = {1: 'one', 2: 'two'}
new = original.copy()
new.clear()
print('Original: ', original)
print('New: ', new)

original = {1: 'one', 2: 'two'}
new = original.copy()
original.clear()
print('Original: ', original)
print('New: ', new)


# =

original = {1: 'one', 2: 'two'}
new = original
new.clear()
print('Original: ', original)
print('New: ', new)
