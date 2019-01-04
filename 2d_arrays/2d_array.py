# Complete the hourglassSum function below.
arr = [-9, -9, -9, 1, 1, 1, 0, -9, 0, 4, 3, 2, -9, -9, -9, 1, 2, 3,
       0, 0, 8, 6, 6, 0, 0, 0, 0, -2, 0, 0, 0, 0, 1, 2, 4, 0]

# arr = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3],
#        [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]


def hourglassSum(arr):
    pass


def find_coordinates(width, index):

    x = index % 6
    y = index // 6
    index += 1

    coordinates = (x, y)
    print(coordinates)
    return coordinates


def find_my_cell(x, y, arr):

    number = arr[(y * 6) + x]

    return number


'''
first hourglass is:
-9 -9 -9
   -9
-9 -9 -9
'''

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
    assert find_my_cell(3, 1, arr) == 4


def test_find_coordinates():
    assert find_coordinates(6, 3) == (3, 0)


def test_find_coordinates():
    assert find_coordinates(6, 16) == (4, 2)
