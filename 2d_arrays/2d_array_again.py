# Complete the hourglassSum function below.
arr = [0, 0, 0, 1, 0, 2, 0, 3, 1, 0, 1, 1, 1, 2, 1, 3]


def conversion_1d_to_2d_array(arr):
    pass


# TESTS


def test_conversion_1d_to_2d():
    assert conversion_1d_to_2d_array(arr) == [(0, 0), (0, 1), (0, 2), (0, 3),
                                              (1, 0), (1, 1), (1, 2), (1, 3)]
