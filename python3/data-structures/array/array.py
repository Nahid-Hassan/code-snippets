# import array module
import array

# declare an array
arr = array.array('i', [1, 2, 3])

# print the original array using for loop
for i in range(3):
    print(arr[i], end=' ')
print('\r')

print(arr.itemsize)  # return the length of a item in bytes
print(arr.typecode)  # return the type code
print(arr.buffer_info())  # return a tuple (address, length)
print(arr.buffer_info()[1] * arr.itemsize)  # 3 * 4 => 12
print(arr.count(3))  # return the number of occurrence of 3 in the array.


# array append(value)
arr.append(4)
print(arr)

# array insert(index_position, value)
arr.insert(2, 10)  # insert 10 in 3rd postion
print(arr)
# insert in last position. if index_position is greater then length size then insert in last position like append method
arr.insert(100, 20)

print(arr)

# array pop(position) : remove the element at that postion and return the value
ret_value = arr.pop(2)
print(ret_value)
print(arr)

# array remove(value) : remove the first occurrence value in this array, if element not found raise a ValueError
arr.remove(1)
print(arr)


# array index(value): return the first occurrence of the given value in the array if not found raise an ValueError.
print(arr.index(4))

# array reverse(): reverse the array items
arr.reverse()
print(arr)

arr.reverse()
print(arr)