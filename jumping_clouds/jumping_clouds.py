# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the jumpingOnClouds function below


def jumpingOnClouds(c):

    jumps = 0

    while len(c):
        if (len(c)) == 1:
            break
        if c[0] == 0:
            jumps += 1
            c.pop(0)
            if (len(c)) > 1:
                c.pop(0)
        if c[0] == 1:
            jumps += 1
            c.pop(0)

    print('Emma does ' + str(jumps) + ' jumps')
    return jumps

# 3
# jumpingOnClouds([0, 0, 0, 0, 0, 0, 0])
# 4
# jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
# 3
# jumpingOnClouds([0, 0, 0, 0, 1, 0])
# 3
jumpingOnClouds([0, 1, 0, 0, 1, 0])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     c = list(map(int, input().rstrip().split()))

#     result = jumpingOnClouds(c)

#     fptr.write(str(result) + '\n')

#     fptr.close()
