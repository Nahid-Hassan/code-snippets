"""
    The bytearray() method returns a bytearray object which is an array of the given bytes.
    
    The syntax of bytearray() method is:
        bytearray([source[, encoding[, errors]]])
            bytearray() method returns a bytearray object which is mutable (can be modified) sequence of integers in the range 0 <= x < 256.
"""

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

size = 5

arr = bytearray(size)
print(arr)

rList = [1, 2, 3, 4, 5]

arr = bytearray(rList)
print(arr)
