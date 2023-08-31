import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f'Function {func.__name__} took {end_time - start_time:.4f} seconds to execute')
        return result
    return wrapper

@timeit
def slow_function():
    time.sleep(2)
    return 'Done'

slow_function()
print(slow_function.__name__) # without wraps -> wrapper
print(slow_function.__name__) # with wraps -> slow_function