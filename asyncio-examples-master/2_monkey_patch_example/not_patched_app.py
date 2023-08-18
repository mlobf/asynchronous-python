import gevent
import requests
import timeit
import datetime

print(datetime.datetime.now())

def make_request(pid):
    requests.get('http://google.com')  # blocking action on the interpreter
    print(f'Process {pid}')


def synchronous():
    for i in range(1, 100):
        make_request(i)


def asynchronous():
    threads = []
    for i in range(1, 100):
        threads.append(gevent.spawn(make_request, i))  # bundles all of the threads (greenlets) in a queue
    gevent.joinall(threads)  # executes threads within the queue


print(f'Synchronous: {timeit.timeit(synchronous, number=1)}')
print(f'Asynchronous: {timeit.timeit(asynchronous, number=1)}')
