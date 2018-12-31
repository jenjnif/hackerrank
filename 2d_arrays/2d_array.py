# Complete the hourglassSum function below.
arr = [-9, -9, -9, 1, 1, 1, 0, -9, 0, 4, 3, 2, -9, -9, -9, 1, 2, 3,
       0, 0, 8, 6, 6, 0, 0, 0, 0, -2, 0, 0, 0, 0, 1, 2, 4, 0]

# arr = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3],
#        [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]


def hourglassSum(arr):
    column_counter = 1
    hourglass = []
    row_counter = 1

    for number in arr:
        if column_counter > 3:
            if column_counter == 6:
                column_counter = 1
                row_counter += 1
            else:
                column_counter += 1
        else:
            if row_counter == 1 or row_counter == 3:
                hourglass.append(number)
                column_counter += 1
            if row_counter == 2:
                if column_counter == 2:
                    hourglass.append(number)
                    column_counter += 1
                else:
                    column_counter += 1
            else:
                continue
    print(hourglass)
    return hourglass


'''first hourglass is:
-9 -9 -9
   -9
-9 -9 -9
'''

# Test that I can list all the cells in the hourglass for each example
# position in the grid
def test_list_hourlgass_numbers():
    assert hourglassSum(arr) == [-9, -9, -9, -9, -9, -9, -9]
