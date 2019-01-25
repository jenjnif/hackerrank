
def find_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
        print(i)
    print(primes)
    return primes


def is_prime(x):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
    return prime


def test_list_first_prime():
    assert find_primes(2) == [2]


def test_list_two_primes():
    assert find_primes(3) == [2, 3]


def test_list_all_primes_1():
    assert find_primes(10) == [2, 3, 5, 7]


def test_list_all_primes_2():
    assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
