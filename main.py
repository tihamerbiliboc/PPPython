import asyncio

import prime_generator
import timeit
import multiprocessing
import time
from joblib import Parallel, delayed
import gui_prime

if __name__ == '__main__':
    min_value = 1
    max_value = 100
    
    start = timeit.default_timer()
    prime_generator.generate_primes_sequential(min_value, max_value)
    stop = timeit.default_timer()
    execution_time = stop - start
    print("Program Executed in " + str(execution_time) + "  seconds")

    start = timeit.default_timer()
    prime_generator.generate_primes_multiprocessing(min_value, max_value)
    stop = timeit.default_timer()
    execution_time = stop - start
    print("Program Executed in " + str(execution_time) + "  seconds")

    start = timeit.default_timer()
    prime_generator.generate_primes_joblib(min_value, max_value)
    stop = timeit.default_timer()
    execution_time = stop - start
    print("Program Executed in " + str(execution_time) + "  seconds")


    # k = input()

    gui_prime.main(asyncio.get_event_loop())
    



