"""
    The chr() method returns a character (a string) from an integer (represents unicode code point of the character).
    
    The syntax of chr() is:
        chr(i)
"""

# you need to specify chr( in range(0x110000) )

print(chr(1))
print(chr(32))
print(chr(100))
print(chr(2113))

print(chr(-1))

try:
    print(chr(-1))
except ValueError as ve:
    print(ve)

# ord() is the reverse function of chr() function.