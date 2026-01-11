from functools import wraps
import time
def decorator(func):
    def wrapper():
        print("Something is happenng before")
        func()
        print("Something is happening after")

    return wrapper

def say_whee():
    print("Whee")


def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finshed {func.__name__}() in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def waste_time(num_times):
    for _ in range(num_times):
        sum([number ** 2 for number in range(10000)])

waste_time(1)
waste_time(100)
#say_whee = decorator(say_whee)

#say_whee()
#print(say_whee)