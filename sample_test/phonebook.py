# use input:
# n, e.g. 3  to represent the number of names and numbers
# then n, number of names and numbers
# Guy 444444
# Tom 555555
# Mat 666666
# create a phone book (dictionary) with these
# then the input queries the dictionary with a name, x times
# and returns the entry if the name is in the dictionary
# e.g. Sam returns 'Not found' and Guy returns Guy=444444
# example input:
# 3
# Guy 444444
# Tom 555555
# Mat 666666
# Sam
# Guy
# Phil
# Tom
# Jon

# example output
# Guy=444444
# Tom=555555

phone_book = {}
try:
    for i in range(int(input())):
        n = input()
        name_number = n.split(' ')
        name = name_number[0]
        number = int(name_number[1])
        phone_book.update({name: number})
    while True:
        n = input()
        if n in phone_book.keys():
            print(n + '=' + str(phone_book[n]))
        else:
            print('Not found')
except EOFError:
    pass
