# Python Data Structure

## Array

### Introduction to array in Python

Other than some generic containers like list, Python in its definition can also handle containers with specified data types. The array can be handled in python by a module named “array“. They can be useful when we have to manipulate only a specific data type values.
Operations on Array :

1. array(data type, value list):- This function is used to create an array with data type and value list specified in its arguments. Some data types are mentioned in the table below.

| Type Code | C Type             | Python Type       | Minimum size in Bytes |
| :-------: | :----------------- | :---------------- | :-------------------: |
|    `b`    | signed char        | int               |           1           |
|    `B`    | unsigned char      | int               |           1           |
|    `u`    | Py_UNICODE         | unicode character |           2           |
|    `h`    | signed short       | int               |           2           |
|    `H`    | unsigned short     | int               |           2           |
|    `i`    | signed int         | int               |           2           |
|    `I`    | unsigned int       | int               |           2           |
|    `l`    | signed long        | int               |           4           |
|    `L`    | unsigned long      | int               |           4           |
|    `q`    | signed long long   | int               |           8           |
|    `Q`    | unsigned long long | int               |           8           |
|    `f`    | float              | float             |           4           |
|    `d`    | double             | float             |           8           |

**Demo Code**:

```Python
# import array module
from array import array

# create an array variable
arr =  array('i', [1, 2, 3, 4])

# print the array
print(arr)
# array('i', [1, 2, 3, 4])
```

**Array methods**:

`append`, `buffer_info`, `byteswap`, `count`, `extend`, `frombytes`, `fromfile`, `fromlist`, `fromstring`, `fromunicode`, `index`, `insert`, `itemsize`, `pop`, `remove`, `reverse`, `tobytes`, `tofile`, `tolist`, `tostring`, `tounicode`, `typecode`
