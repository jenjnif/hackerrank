# Complete the hourglassSum function below.
arr = [-9, -9, -9, 1, 1, 1, 0, -9, 0, 4, 3, 2, -9, -9, -9, 1, 2, 3,
       0, 0, 8, 6, 6, 0, 0, 0, 0, -2, 0, 0, 0, 0, 1, 2, 4, 0]


def find_width(arr):

    total_length_list = len(arr)
    width = total_length_list**(0.5)

    return width


def find_coordinates(index):
    pass


# TESTS


def test_width():
    assert find_width(arr) == 6


def test_coordinates():
    assert find_coordinates(arr[3]) == (3, 0)
