"""
    The delattr() deletes an attribute from the object (if the object allows it).

    delattr(object, name)
        * object - the object from which name attribute is to be removed
        * name -  a string which must be the name of the attribute to be removed from the object
"""


class Coordinate:
    x = 10
    y = -5
    z = 30


point1 = Coordinate()


print("-- Before deleting z --")
print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)


a = delattr(Coordinate, 'z')
print(a)  # None, nothing return

print("-- After deleting z --")
print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)


# using del keyword
class Coordinate:
    x = 10
    y = -5
    z = 30


point1 = Coordinate()


print("-- Before deleting z --")
print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

del Coordinate.z

print("-- After deleting z --")
print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)
