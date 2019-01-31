# represent a decimal number, n, as binary
# then calculate the number of consecutive 1's
# e.g. 5 is 101 in binary with 1 consecutive 1
# e.g. 6 is 110 in binary with 2 consecutive 1's


def list_binary(n):
    binary = []
    number = 1
    while number < n:
        binary.append(number)
        number = number * 2
    return binary[::-1]


def decimal_binary(n):
    binary_number = []
    for i in list_binary(n):
        if n - i >= 0:
            print('n = ', n)
            print('i = ', i)
            binary_number.append(1)
            n -= i
        else:
            binary_number.append(0)
            print('correct?')
    return binary_number


# 10 is 1010
#       8020
print(decimal_binary(10))
