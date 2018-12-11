# Complete the countingValleys function below.
def countingValleys(n, s):

    elevation = 0
    valleys = 0
    first_time_valley = None
    for step in s:
        if 'D' in step:
            elevation -= 1
            print(elevation)
            if elevation == -1:
                first_time_valley = True
        elif 'U' in step:
            elevation += 1
            print(elevation)
            if first_time_valley is True:
                if elevation == 0:
                    first_time_valley = False
                    valleys += 1
    valleys = "You have walked through " + str(valleys) + ' valleys.'
    return valleys


# print(countingValleys(8, ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']))
print(countingValleys(10, ['D', 'U', 'D', 'D', 'D', 'U', 'U', 'D', 'U', 'U']))

# \/\       /
#     \. /\/
#      \/.
# D is a step down and U is a step up. A valley is only complete if going from
# sea level (i.e. elevation 0) down at least two consecutive sgeps and then
# back up to sea level again.
