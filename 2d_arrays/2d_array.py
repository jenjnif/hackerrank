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


# TESTS


def test_width():
    assert find_width(arr) == 6


def test_coordinates():
    assert find_coordinates(3) == (3, 0)
