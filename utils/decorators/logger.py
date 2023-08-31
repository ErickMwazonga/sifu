import logging

def logger(func):
    def wrapper(*args, **kwargs):
        arg_str = ', '.join([str(arg) for arg in args])
        logging.info(f'Calling function: {func.__name__} with args: {arg_str}')

        result = func(*args, **kwargs)
        logging.info(f'Function {func.__name__} executed')
        return result
    
    return wrapper

logging.basicConfig(level=logging.INFO)


@logger
def add(a, b):
    return a + b

add(10, 4)


