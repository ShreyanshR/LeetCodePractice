from functools import cache, wraps

def log(func):
    if getattr(func, "_log", False):
        return func
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result, end='')
        return result
    
    wrapper._log = True
    return wrapper

@log
@cache
@log
def foo(a):
    return a
    
foo(1)
foo(2)
foo(1)