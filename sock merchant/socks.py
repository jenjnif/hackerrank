def sockMerchant(n, ar):

    sock_dictionary = {}
    colour = None
    pairs = 0
    for sock in range(len(ar)):
        colour = ar[sock]
        if int(colour) in sock_dictionary:
            sock_dictionary[colour] += 1
            if sock_dictionary[colour] == 2:
                pairs += 1
                del sock_dictionary[colour]
        else:
            sock_dictionary[ar[sock]] = 1
    print(pairs)
    return pairs


sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
