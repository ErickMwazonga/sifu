# 1. Timing/Performance Measurement:
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper


# 2. Retry Logic:
def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    time.sleep(delay)
                    print(f"Retrying {func.__name__}, attempt {attempts}")
        return wrapper
    return decorator

# 3. Input Validation:
def validate_args(validator):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not validator(*args, **kwargs):
                raise ValueError("Invalid arguments")
            return func(*args, **kwargs)
        return wrapper
    return decorator
   

# 4. Logging:
import logging

def log_function_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper
   

# 5. Rate Limiting:
def rate_limit(calls_per_second=1):
    min_interval = 1.0 / calls_per_second
    last_called = [0.0]
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator
   

# 6. Memoization/Caching (similar to lru_cache but customized):
def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper
   

# 7. Authorization/Permission Checking:
def require_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if permission not in user.permissions:
                raise PermissionError(f"User lacks required permission: {permission}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
   
# 8. Deprecation Warning:
import warnings

def deprecated(reason):
    def decorator(func):
        def wrapper(*args, **kwargs):
            warnings.warn(f"{func.__name__} is deprecated: {reason}", 
                        category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator
   

# 9. Transaction Management:
def transactional(func):
    def wrapper(db_connection, *args, **kwargs):
        try:
            db_connection.begin_transaction()
            result = func(db_connection, *args, **kwargs)
            db_connection.commit()
            return result
        except Exception as e:
            db_connection.rollback()
            raise
    return wrapper



def return_none_if_empty(method):
    def wrapper(self, *args, **kwargs):
        if self.is_empty():
            return None
        return method(self, *args, **kwargs)
    return wrapper

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def is_empty(self):
        return len(self.stack) == 0

    @return_none_if_empty
    def pop(self):
        return self.stack.pop()

    @return_none_if_empty
    def top(self):
        return self.stack[-1]

    @return_none_if_empty
    def getMin(self):
        curr_min = self.stack[0]
        for index in range(1, len(self.stack)):
            curr_min = min(self.stack[index], curr_min)
        return curr_min
