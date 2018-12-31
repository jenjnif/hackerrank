# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    number_leftover = n % len(s)
    whole_times_repeated = n // len(s)
    string_left = s[:number_leftover]
    main_counter = 0
    leftover_counter = 0

    for letter in s:
        if 'a' == letter:
            main_counter += 1

    for letter in string_left:
        if 'a' == letter:
            leftover_counter += 1

    total_string = main_counter * whole_times_repeated + leftover_counter

    print(total_string)
    return total_string

# 7
# repeatedString('aba', 10)
# 1000000000000
# repeatedString('a', 1000000000000)
# 15
repeatedString('abaa', 20)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     n = int(input())

#     result = repeatedString(s, n)

#     fptr.write(str(result) + '\n')

#     fptr.close()
