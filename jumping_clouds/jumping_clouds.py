# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):

    jumps = 0
    skip = None

    for steps in range(len(c)):
        print(c[steps])
        if c[steps] == 0:
            if skip is True:
                jumps += 1
                skip = False
                print('plus a jump ' + str(jumps))
            else:
                skip = True
        else:
            if skip is False:
                jumps += 2
                print('plus two jumps ' + str(jumps))
            else:
                jumps += 1
                print('plus a jump ' + str(jumps))

    print('Emma does ' + str(jumps) + ' jumps')
    return jumps


# jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
# jumpingOnClouds([0, 0, 0, 0, 1, 0])
jumpingOnClouds([0, 1, 0, 0, 1, 0])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     c = list(map(int, input().rstrip().split()))

#     result = jumpingOnClouds(c)

#     fptr.write(str(result) + '\n')

#     fptr.close()
