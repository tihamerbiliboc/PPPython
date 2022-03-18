import math


def is_prime(input_number):
    if input_number == 1:
        return False
    if input_number % 2 == 0 and input_number > 2:
        return False
    boundary = math.floor(math.sqrt(input_number))
    for x in range(3, boundary + 1, 2):
        if input_number % x == 0:
            return False
    return True


def generate_primes(min_value, max_value):
    prime_list = []
    for x in range(min_value, max_value + 1):
        if is_prime(x):
            prime_list.append(x)

    prime_list.sort()
    return prime_list
