# Complete the hourglassSum function below.
arr = [-9, -9, -9, 1, 1, 1, 0, -9, 0, 4, 3, 2, -9, -9, -9, 1, 2, 3,
       0, 0, 8, 6, 6, 0, 0, 0, 0, -2, 0, 0, 0, 0, 1, 2, 4, 0]


# -9, -9, -9,  1,  1,  1
#  0, -9,  0,  4,  3,  2
# -9, -9, -9,  1,  2,  3,
#  0,  0,  8,  6,  6,  0
#  0,  0,  0, -2,  0,  0
#  0,  0,  1,  2,  4,  0


def hourglassSum(arr):

    width = int(len(arr)**(0.5))
    index = 0
    total_sum = 0
    for i in arr:
        x = int(index % width)
        y = int(index // width)
        if x < 4 and y < 4:
            hourglass = []
            top = arr[index:index + 3]
            for number in top:
                hourglass.append(number)
            middle = int(arr[index + width + 1])
            hourglass.append(middle)
            bottom = arr[index + width*2:index + width*2 + 3]
            for number in bottom:
                hourglass.append(number)
            sum_hourglasses = int(sum(hourglass))
            if sum_hourglasses > total_sum:
                total_sum = sum_hourglasses
        index += 1
    return total_sum


# arr_two = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3],
#            [0, 0, 10, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]

arr_two = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5],
           [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5],
           [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]

# -9, -9, -9,  1,  1,  1
#  0, -9,  0,  4,  3,  2
# -9, -9, -9,  1,  2,  3,
#  0,  0,  8,  6,  6,  0
#  0,  0,  0, -2,  0,  0
#  0,  0,  1,  2,  4,  0


def hourglassSum_twod(arr_two):
    x = 0
    y = 0
    counter = 0
    hourglasses = []
    for items in arr_two:
        for items in arr_two[counter]:
            if y < 4 and x < 4:
                hourglass_top = sum(arr_two[x][y:y + 3])
                hourglass_mid = arr_two[x + 1][y + 1]
                hourglass_bot = sum(arr_two[x + 2][y:y + 3])
                hourglass_tot = hourglass_top + hourglass_mid + hourglass_bot
                hourglasses.append(hourglass_tot)
                y += 1
        counter += 1
        y = 0
        x += 1
    return max(hourglasses)

                # if hourglass_tot > total_sum:
                #     total_sum = hourglass_tot

# TESTS


def test_total_sum():
    assert hourglassSum(arr) == 28


def test_hourglassSum_twod():
    assert hourglassSum_twod(arr_two) == -6
