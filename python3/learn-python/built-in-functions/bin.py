"""
    bin(num): The bin() method converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement __index__() method to return an integer.

    num:
        int: an integer number whose binary equivalent is to be calculated.
             If not an integer, should implement __index__() method to return an integer.

    Note:
        If not specified an integer, it raises a TypeError exception highlighting the type cannot be interpreted as an integer.
"""
number = 30
bin_rep = bin(number)

print(bin_rep)  # 0b11110
# The prefix 0b represents that the result is a binary string.
print(type(bin_rep))  # <class 'str'>


"""
    Convert an object to binary implementing __index__() method
"""

class Quantity:
    apple = 1
    orange = 2
    grapes = 3

    def __index__(self):
        return self.orange + self.apple + self.grapes
    
    # def __repr__(self):
    #     return "Quantity class"

print(Quantity())
print(bin(Quantity()))
# Quantity()

class Float:
    float_number = 32.54

    def __index__(self):
        return int(self.float_number)

print(bin(Float()))

class String:
    str_obj = '0814341'

    def __index__(self):
        return int(self.str_obj)

print(bin(String()))