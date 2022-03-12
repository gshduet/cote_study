from time import time


def time_check(solution):

    def wrapper(*args, **kwargs):
        
        start_time = time()
        end_time = time()

        print(f'operating time = {end_time - start_time}')
        return solution(*args, **kwargs)

    return wrapper
