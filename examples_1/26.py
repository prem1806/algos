def is_prime(a):
    print all(a % i for i in range(2, a))

is_prime(int(raw_input()))


