
def find_primes(n):
    primes = []
    for i in range(2, n):
        primes.append(i)
        print(primes)
    return primes


def test_list_primes():
    assert find_primes(3) == [2]
