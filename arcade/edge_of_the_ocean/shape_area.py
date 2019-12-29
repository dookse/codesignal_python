def shape_area(n):
    result = 1
    for i in range(1, n):
        result += 4 * i
    return result


print(shape_area(4))
