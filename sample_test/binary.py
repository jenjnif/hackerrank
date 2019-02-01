# represent a decimal number, n, as binary
# then calculate the number of consecutive 1's
# e.g. 5 is 101 in binary with 1 consecutive 1
# e.g. 6 is 110 in binary with 2 consecutive 1's


def decimal_to_binary_consecutive_ones(n):
    bit = []
    counter = 0
    consecutive = [0]
    while n > 0:
        bit.append(n % 2)
        n = n // 2
    binary = bit[::-1]
    for i in range(len(binary)):
        if binary[i] == 1:
            counter += 1
        else:
            consecutive.append(counter)
            counter = 0
    if counter > 0:
        consecutive.append(counter)
    return max(consecutive)


# 34 is 100010
# 6 is 110
# 355 is 101100011
# 5 is 11
# 367 is 101101111
print(decimal_to_binary_consecutive_ones(367))
