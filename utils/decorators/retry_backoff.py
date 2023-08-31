import time
import random

MAX_DELAY_IN_SECONDS = 60

def backoff(max_retries, base_delay=1, max_delay=MAX_DELAY_IN_SECONDS):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'Attempt {retries + 1}: {e}')
                    retries += 1
                    # delay = min(base_delay * (2 ** retries), max_delay)
                    # print(f'Retrying in {delay} seconds...')

                    delay = (base_delay * 2 ** retries + random.uniform(0, 1))
                    print(f'Retrying in {delay:.2f} seconds...')

                    time.sleep(delay)

            raise Exception('Max retries reached, operation failed.')

        return wrapper

    return decorator


@backoff(max_retries=5, base_delay=1)
def perform_operation():
    if random.random() < 0.8:
        raise Exception('Network error')
    return 'Success'


try:
    result = perform_operation()
    print('Operation succeeded:', result)
except Exception as e:
    print('Operation failed:', e)