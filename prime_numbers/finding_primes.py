
def find_primes(n):
    primes = [2]
    p = 2
    for i in range(2, n):
        if i % p != 0:
            primes.append(i)
    print(primes)
    return primes


def test_list_first_prime():
    assert find_primes(3) == [2]


def test_list_two_primes():
    assert find_primes(5) == [2, 3]


def test_list_all_primes_n():
    assert find_primes(10) == [2, 3, 5, 7]
