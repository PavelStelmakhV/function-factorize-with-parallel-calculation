from multiprocessing import Process, Manager
from time import time
import sys


def find_divisors(number: int, m):
    result = []
    for i in range(1, number+1):
        if number % i == 0:
            result.append(i)
    m[number] = result
    sys.exit(0)


def factorize_process_manager(*number):
    result = []
    process = []
    manager = Manager()
    m = manager.dict()
    for num in number:
        pr = Process(target=find_divisors, args=(num, m))
        process.append(pr)
    [pr.start() for pr in process]
    [pr.join() for pr in process]

    for num in number:
        result.append(m[num])
    return result


if __name__ == '__main__':

    timer = time()
    a, b, c, d = factorize_process_manager(128, 255, 99999, 10651060)
    print(f'Time for processes computing with manager: {round(time() - timer, 6)}')
    print(f'{a}\n{b}\n{c}\n{d}\n')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
