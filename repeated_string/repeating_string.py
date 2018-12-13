# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    number_leftover = n % len(s)
    print(number_leftover)
    whole_times_repeated = n // len(s)
    print(whole_times_repeated)
    string_left = s[0:number_leftover]
    print(string_left)
    a_counter = 0
    leftover_counter = 0

    for letter in s:
        if 'a' in letter:
            a_counter += 1
            print(a_counter)

    for letter in string_left:
        if 'a' in letter:
            leftover_counter += 1
            print('here is ' + str(leftover_counter))

    total_string = a_counter * whole_times_repeated + leftover_counter

    print(total_string)

# 7
# repeatedString('aba', 10)
# # 1000000000000
repeatedString('a', 1000000000000)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     n = int(input())

#     result = repeatedString(s, n)

#     fptr.write(str(result) + '\n')

#     fptr.close()
