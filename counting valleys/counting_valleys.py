#!/bin/python3

import os


# Complete the countingValleys function below.
def countingValleys(n, s):

    # if __name__ == '__main__':
    #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #     n = int(input())
    #     s = input()
    level = 0
    valleys = 0
    first_time_valley = None
    for step in s:
        if 'D' in step:
            level -= 1
            print(level)
            if level == -2:
                first_time_valley = True
        elif 'U' in step:
            level += 1
            print(level)
            if first_time_valley is True:
                if level == 0:
                    first_time_valley = False
                    valleys += 1

    print("You have walked through " + str(valleys) + " valleys.")


# result = countingValleys(n, s)
# fptr.write(str(result) + '\n')

    #     # fptr.close()
    # print(level)


countingValleys(8, ['D', 'D', 'D', 'U', 'U', 'U'])
# countingValleys(8, ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U'])
