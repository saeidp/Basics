def swap(array, first_index, second_index):
    array[first_index], array[second_index] = array[second_index], array[first_index]
    return array


array = swap([1, 2], 0, 1)
print(array)
