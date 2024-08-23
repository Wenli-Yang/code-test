# Review 1

#def add_to_list(value, my_list=[]): variable potential risks, better to use None
def add_to_list(value, my_list):    
    if isinstance(my_list, list):
        my_list.append(value)
    else:
        raise TypeError("my_list must be a list")
    return my_list


# Review 2

def format_greeting(name, age):
    #return "Hello, my name is {name} and I am {age} years old." wrong str input format
    return f"Hello, my name is {name} and I am {age} years old."


# Review 3

class Counter:
    count = 0

    def __init__(self):
        #self.count += 1
        Counter.count += 1

    def get_count(self):
        #return self.count
        return Counter.count


# Review 4

import threading


class SafeCounter:

    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    threads.append(t)
    t.start()

    threads.append(t)

for t in threads:
    t.join()


# Review 5

def count_occurrences(lst):
    counts = {}

    for item in lst:

        if item in counts:

            counts[item] += 1

        else:

            counts[item] = 1

    return counts