# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    infinite_string = ''
    a_counter = 0

    while len(infinite_string) < n:
        for letter in s:
            if len(infinite_string) <= n:
                infinite_string += letter
    for letter in infinite_string:
        if 'a' in letter:
            a_counter += 1

    print(a_counter)
    return a_counter

# 7
# repeatedString('aba', 10)
# 1000000000000
repeatedString('a', 1000000000000)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     n = int(input())

#     result = repeatedString(s, n)

#     fptr.write(str(result) + '\n')

#     fptr.close()
