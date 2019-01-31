# represent a decimal number, n, as binary
# then calculate the number of consecutive 1's
# e.g. 5 is 101 in binary with 1 consecutive 1
# e.g. 6 is 110 in binary with 2 consecutive 1's


def convert_decimal_binary(n):
    bit = []
    while n > 0:
        bit.append(n % 2)
        n = n // 2
    return bit[::-1]


# 34 is 100010
print(convert_decimal_binary(34))
