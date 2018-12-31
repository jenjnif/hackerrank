
number = None


def findNumber(arr, k):
    if k in arr:
        number = True
    else:
        number = False

    if number is True:
        print('yes')
        return"YES"
    else:
        print("no")
        return "NO"


findNumber([1, 2, 3, 4, 5], 66)
