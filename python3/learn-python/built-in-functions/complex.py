"""
    The complex() method returns a complex number when real and imaginary parts are provided, or it converts a string to a complex number.

    complex([real[, imag]])
        * real - real part. If real is omitted, it defaults to 0.
        * imag - imaginary part. If imag is omitted, it defaults to 0.
"""

z = complex(2, -3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)

a = 2+3j
print('a =', a)
print('Type of a is', type(a))

b = -2j
print('b =', b)
print('Type of b is', type(a))

c = 0j
print('c =', c)
print('Type of c is', type(c))


print(z)
print(z.real)
print(z.imag)