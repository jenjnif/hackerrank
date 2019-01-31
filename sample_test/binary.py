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
    for i in list_binary(n):
        print(i)


# 10 is 01010
print(decimal_binary(10))
