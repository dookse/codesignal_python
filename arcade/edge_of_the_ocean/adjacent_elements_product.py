def adjacent_elements_product(input_array):
    return max([input_array[i] * input_array[i + 1] for i in range(len(input_array) - 1)])


print(adjacent_elements_product([3, 6, -2, -5, 7, 3]))
