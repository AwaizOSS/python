# Problem: Write a decorator that measures the time a function takes to execute.

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start}")
        return result

    return wrapper


@timer
def ex_func(n):
    time.sleep(n)


# ex_func(3)


# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.
def details(func):
    def wrapper(*args, **kwargs):
        args_string = ", ".join(str(arg) for arg in args)
        # the statment in join() is called comprehension or reverse loop or generator expression which is ofcourse an iterable as join accepts only iterables, where it is returning arg converted to string
        kwargs_string = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"{func.__name__} has args: {args_string} and kwargs: {kwargs_string}")
        return func(*args, **kwargs)

    return wrapper


@details
def ex2(x, y):
    pass


# ex2(1, 2)


# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
def cache(func):
    cache_value = {}

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        else:
            result = func(*args)
            cache_value[args] = result
            print(cache_value)
            return result

    return wrapper


@cache
def ex3(x, y):
    time.sleep(2)
    return x + y


print(ex3(1, 2))
print(ex3(1, 2))
print(ex3(1, 3))
