import array


# using temporary variable
def temp_array_rotaion(data, d, n):
    temp = []

    for _ in range(d):
        # append first item into the temp list.
        temp.append(data[0])
        # pop the first item from the data
        data.pop(0)

    # Now append temp into data
    data.fromlist(temp)
    return data


if __name__ == "__main__":
    data = array.array('i', [1, 2, 3, 4, 5, 6, 7])
    data = temp_array_rotaion(data, 2, data.buffer_info()[1])
    print(data)
