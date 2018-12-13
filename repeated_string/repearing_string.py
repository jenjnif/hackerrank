# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    a_counter = 0

    for letter in s:
        if 'a':
            a_counter += 1

    return a_counter

# 7
# repeatedString(aba, 10)
# 1000000000000
# repeatedString(a, 1000000000000)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     n = int(input())

#     result = repeatedString(s, n)

#     fptr.write(str(result) + '\n')

#     fptr.close()
