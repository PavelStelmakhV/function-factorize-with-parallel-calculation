from time import time
import concurrent.futures
from multiprocessing import Pool


def find_divisors(number: int):
    results = []
    for i in range(1, number+1):
        if number % i == 0:
            results.append(i)
    return results


def factorize(*number):
    results = []
    for num in number:
        results.append(find_divisors(num))
    return results


def factorize_thread_async(*number):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for r in executor.map(find_divisors, number):
            results.append(r)
    return results


def factorize_process_async(*number):
    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for r in executor.map(find_divisors, number):
            results.append(r)
    return results


def factorize_process_pool(*number):
    with Pool(processes=len(number)) as pool:
        results = pool.map(find_divisors, number)
    return results


if __name__ == '__main__':

    timer = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f'Time for normal computing: {round(time() - timer, 6)}')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    # --------------- Threads ---------------
    timer = time()
    a, b, c, d = factorize_thread_async(128, 255, 99999, 10651060)
    print(f'Time for asynchronous computing: {round(time() - timer, 6)}')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    # --------------- Processes ---------------
    timer = time()
    a, b, c, d = factorize_process_async(128, 255, 99999, 10651060)
    print(f'Time for async processes computing: {round(time() - timer, 6)}')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    # --------------- Processes ---------------
    timer = time()
    a, b, c, d = factorize_process_pool(128, 255, 99999, 10651060)
    print(f'Time for pool processes computing: {round(time() - timer, 6)}')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
