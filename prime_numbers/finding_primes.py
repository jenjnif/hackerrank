
def find_primes(n):
    primes = []
    p = 2
    for i in range(2, n):
        primes.append(i)
        print(primes)
    return primes


def test_list_first_prime():
    assert find_primes(3) == [2]
