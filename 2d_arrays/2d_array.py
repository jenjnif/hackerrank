# Complete the hourglassSum function below.
arr = [-9, -9, -9, 1, 1, 1, 0, -9, 0, 4, 3, 2, -9, -9, -9, 1, 2, 3,
       0, 0, 8, 6, 6, 0, 0, 0, 0, -2, 0, 0, 0, 0, 1, 2, 4, 0]


def find_width(arr):

    total_length_list = len(arr)
    width = int(total_length_list**(0.5))
    return width


def find_coordinates(index):

    width = find_width(arr)
    x = int(index % width)
    y = int(index // width)
    coordinates = (x, y)
    return coordinates


def find_hourglass(coordinates):

    width = find_width(arr)
    hourglass = []
    x = coordinates[0]
    y = coordinates[1]

    for i in range(3):
        hourglass_top = arr[(y * width) + x]
        x += 1
        hourglass.append(hourglass_top)

    y += 1
    x -= 2
    for i in range(1):
        hourglass_middle = arr[(y * width) + x]
        hourglass.append(hourglass_middle)

    y += 1
    x -= 1
    for i in range(3):
        hourglass_bottom = arr[(y * width) + x]
        x += 1
        hourglass.append(hourglass_bottom)
    return hourglass


def sum_hourglasses(arr):

    width = find_width(arr)
    index = 0
    sum_hourglasses = 0
    for number in arr:
        coordinates = find_coordinates(index)
        index += 1
        if coordinates[1] < (width - 2):
            if coordinates[0] < 4:
                next_sum = sum(find_hourglass(coordinates))
                if next_sum > sum_hourglasses:
                    sum_hourglasses = next_sum
        else:
            continue
    return sum_hourglasses


# TESTS


def test_width():
    assert find_width(arr) == 6


def test_coordinates():
    assert find_coordinates(3) == (3, 0)


def test_hourglass():
    assert find_hourglass((0, 0)) == [-9, -9, -9, -9, -9, -9, -9]


def test_sum_hourglasses():
    assert sum_hourglasses(arr) == 28
