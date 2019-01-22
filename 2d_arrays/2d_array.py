# Complete the hourglassSum function below.
arr = [-9, -9, -9, 1, 1, 1, 0, -9, 0, 4, 3, 2, -9, -9, -9, 1, 2, 3,
       0, 0, 8, 6, 6, 0, 0, 0, 0, -2, 0, 0, 0, 0, 1, 2, 4, 0]

# arr = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3],
#        [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]

# 1  2  3  4  5  6
# 7  8  9  10 11 12
# 13 14 15 16 17 18
# 19 20 21 22 23 24
# 25 26 27 28 29 30
# 31 32 33 34 35 36


def find_coordinates(width, index):

    x = index % width
    y = index // width
    coordinates = (x, y)

    return coordinates


def find_width(arr):

    total_length_list = len(arr)
    width = total_length_list**(0.5)

    return width


def last_index(arr):

    total_length_list = len(arr)
    width = find_width(arr)
    last_index = int(total_length_list - (2 * width) - 3)

    return last_index


def find_my_cell(coordinates, arr):

    x = coordinates[0]
    y = coordinates[1]
    number = arr[(y * 6) + x]

    return number


def find_my_hourglass(coordinates, arr):

    hourglass = []
    x = coordinates[0]
    y = coordinates[1]

    for i in range(3):
        if y > 3:
            return None
        else:
            if x > 3 and x < 5:
                return None
            else:
                hourglass_top = arr[(y * 6) + x]
                x += 1
                hourglass.append(hourglass_top)

    y += 1
    x -= 2
    for i in range(1):
        hourglass_middle = arr[(y * 6) + x]
        hourglass.append(hourglass_middle)

    y += 1
    x -= 1
    for i in range(3):
        hourglass_bottom = arr[(y * 6) + x]
        x += 1
        hourglass.append(hourglass_bottom)
    print(hourglass)
    return hourglass


def hourglassSum(arr):
    pass
#     index = 0
#     for position in arr:
#         h = find_my_hourglass(find_coordinates(6, index), arr)
#         # sum(h)
#         index += 1

'''
grid is:
-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
'''


# Test that I can list all the cells in the hourglass for each example
# position in the grid
def test_find_any_cell():
    assert find_my_cell([3, 1], arr) == 4


def test_find_coordinates_one():
    assert find_coordinates(6, 3) == (3, 0)


def test_find_coordinates_two():
    assert find_coordinates(6, 16) == (4, 2)


def test_find_hourglass():
    assert find_my_hourglass((0, 0), arr) == [-9, -9, -9, -9, -9, -9, -9]


def test_width():
    assert find_width(arr) == 6


def test_last_index():
    assert last_index(arr) == 21


# def test_hourglassSum():
#     assert hourglassSum(arr) == 25
