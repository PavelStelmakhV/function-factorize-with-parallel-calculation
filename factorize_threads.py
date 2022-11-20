from threading import Thread
from queue import Queue
from time import time
import logging


def find_divisors(num_queue: Queue, results: Queue):
    result = []
    number = num_queue.get()
    for i in range(1, number+1):
        if number % i == 0:
            result.append(i)
    results.put(result)


def factorize_threads(*number):
    result = []
    num_queue = Queue()
    results = Queue()

    [num_queue.put(num) for num in number]
    if num_queue.empty():
        logging.info('Nothing')
    threads = [Thread(target=find_divisors, args=(num_queue, results)) for _ in range(len(number))]
    [th.start() for th in threads]
    [th.join() for th in threads]
    while not results.empty():
        result.append(results.get())
    return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    timer = time()
    a, b, c, d = factorize_threads(128, 255, 99999, 10651060)
    print(f'Time for threads computing: {round(time() - timer, 6)}')
    # print(f'{a}\n{b}\n{c}\n{d}\n')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
