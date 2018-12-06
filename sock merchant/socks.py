# def sockMerchant(n, ar):

#     sock_dictionary = {}
#     colour = None
#     pairs = 0
#     for sock in range(len(ar)):
#         print(len(ar))
#         print(ar[sock])
#         colour = ar[sock]
#         if int(colour) in sock_dictionary:
#             sock_dictionary[colour] += 1
#             print(sock_dictionary)
#             if sock_dictionary[colour] == 2:
#                 pairs += 1
#                 del sock_dictionary[colour]
#                 print(pairs)
#         else:
#             sock_dictionary[ar[sock]] = 1
#             print(sock_dictionary)
#     return pairs


# sockMerchant(2, [1, 2, 2, 3, 6, 6, 6, 40, 81, 40])

def sockMerchant(n, ar):

    if __name__ == '__main__':
        fptr = open(input.txt, 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))
    sock_dictionary = {}
    colour = None
    pairs = 0
    for sock in range(len(ar)):
        print(len(ar))
        print(ar[sock])
        colour = ar[sock]
        if int(colour) in sock_dictionary:
            sock_dictionary[colour] += 1
            print(sock_dictionary)
            if sock_dictionary[colour] == 2:
                pairs += 1
                del sock_dictionary[colour]
                print(pairs)
        else:
            sock_dictionary[ar[sock]] = 1
            print(sock_dictionary)
    return pairs

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


sockMerchant()
