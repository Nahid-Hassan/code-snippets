"""
    ascii(object): The ascii() method returns a string containing a printable representation of an object.

    object:
        list, string, number etc.
"""

# The non-ASCII characters in the string are escaped using \x, \u or \U.

normal_text = 'Python is awesome!'
print(ascii(normal_text))

other_text = 'Pythön is interesting'
print(ascii(other_text))  # 'Pyth\xf6n is interesting'

randomList = ['Python', 'Pythön', 5, '√']
print(ascii(randomList))
print(ascii(randomList))  # ['Python', 'Pyth\xf6n', 5, '\u221a']
