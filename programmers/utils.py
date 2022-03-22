from time import time


def time_check(solution):

    def wrapper(*args, **kwargs):
        
        start_time = time()
        func = solution(*args, **kwargs)
        end_time = time()

        print(f'operating time = {(end_time - start_time)*1000}')
        return func

    return wrapper
