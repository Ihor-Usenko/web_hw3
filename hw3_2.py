import time
import multiprocessing

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def synchronous_factorize(numbers):
    result = []
    for number in numbers:
        result.append(factorize(number))
    return result

def parallel_factorize(numbers):
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        result = pool.map(factorize, numbers)
    return result

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    result = synchronous_factorize(numbers)
    end_time = time.time()
    time_test1 = end_time - start_time
    print("\nSynchronous result: ")
    for number, factors in zip(numbers, result):
        print(f"Factors of {number}: {factors}")
    
    print(f"Execution Time : {time_test1} seconds")

    start_time = time.time()
    parallel_result = parallel_factorize(numbers)
    end_time = time.time()
    time_test2 = end_time - start_time

    print("\nParallel result: ")
    for number, factors in zip(numbers, parallel_result):
        print(f"Factors of {number}: {factors}")
    print(f"Execution Time : {time_test2} seconds")
