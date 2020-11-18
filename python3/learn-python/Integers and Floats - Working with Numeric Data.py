## Integer Type
num = 3

# type()
print(type(num)) # <class 'int'>

## Float Type
num = 3.14156
print(type(num)) # <class 'float'>


### Arithmetics operator
# Addition            :  3 + 2     ==> 5      
# Subtraction         :  3 - 2     ==> 1
# Multiplication      :  3 * 10    ==> 30
# Division            :  3 / 2     ==> 1.5
# Floor Division:     : 3 // 2     ==> 1   
# Exponent            :  2 ** 3    ==> 8
# Modulus             :  3 % 2     ==> 1


print(3 + 2)      # 5
print(3 - 2)      # 1
print(3 * 2)      # 6
print(3 / 2)      # 1.5
print(3 // 2)     # 1
print(3 ** 2)     # 9
print(3 % 2)      # 1
print(4 % 2)      # 0
print(5 % 2)      # 1

## abs() => return positive value
print(abs(-3)) # 3

## round(float_value)
print(round(3.75)) # 4
print(round(3.45)) # 3

## round(float_value, digit )

'''
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
'''
print(round(3.456))    # 3
print(round(3.456, 1)) # 3.5 
print(round(3.456, 2)) # 3.46
print(round(3.456, 3)) # 3.456

## Comparison Operators

# Equal               :  3  == 2  ==> False
# Not Equal           :  3  != 2  ==> True
# Greater Than        :  3  >  2  ==> True
# Less Than           :  3  <  2  ==> False
# Greater or Equal    :  3  >= 2  ==> True
# Less or Equal       :  3  <= 2  ==> False

print(3  == 2) # False
print(3  != 2) # True
print(3  >  2) # True
print(3  <  2) # False
print(3  >= 2) # True
print(3  <= 2) # False


## Work with something look like a number but it is actually a string

num_1 = '100'
num_2 = '200' 

print(num_1 + num_2) # 100200 # string_concatenate

## so we need casting
num_1 = int('100')
num_2 = int('200')

print(num_1 + num_2) # 300