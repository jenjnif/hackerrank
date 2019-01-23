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
            sum_hourglasses = sum(hourglass)
            if sum_hourglasses > total_sum:
                total_sum = sum_hourglasses
        index += 1
    return(total_sum)


# TESTS


def test_total_sum():
    assert hourglassSum(arr) == 28
