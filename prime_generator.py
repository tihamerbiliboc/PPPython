import math
import threading
import numpy as np
import multiprocessing
from joblib import Parallel, delayed


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


def generate_primes_sequential(min_value, max_value):
    prime_list = []
    for x in range(min_value, max_value + 1):
        if is_prime(x):
            prime_list.append(x)

    #prime_list.sort()
    return prime_list

def generate_primes_parallel(x):
    if is_prime(x):
        return x
    pass
    

def generate_primes_multiprocessing(min_value, max_value):
    prime_list = []
    pool_obj = multiprocessing.Pool(4)
    prime_list = pool_obj.map(generate_primes_parallel, range(min_value,max_value+1))
    #try:
    #    while True:
    #        prime_list.remove(None)
    #except ValueError:
    #    pass
    filtered_list = list(filter(None, prime_list))
    return filtered_list

def generate_primes_joblib(min_value, max_value):
    prime_list = []
    prime_list = Parallel(n_jobs=4)(delayed(generate_primes_parallel)(x) for x in range(min_value, max_value+1))
    #try:
    #    while True:
    #        prime_list.remove(None)
    #except ValueError:
    #    pass
    filtered_list = list(filter(None, prime_list))
    return filtered_list
    


