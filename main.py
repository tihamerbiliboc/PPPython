import prime_generator
import timeit



if __name__ == '__main__':
    start = timeit.default_timer()
    print(prime_generator.generate_primes(10, 1000000))
    stop = timeit.default_timer()
    execution_time = stop - start
    print("Program Executed in " + str(execution_time) + "  seconds")



