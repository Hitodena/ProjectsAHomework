array = [-2, 3, 8, -11, -4, 6]
# Recursion


def negative(list):
    count = 0
    for item in list:
        if item < 0:
            count += 1
        else:
            negative(list[1:])
    return count


print(negative(array))



