from functools import wraps
from time import perf_counter, sleep

def get_time(func):
    """Egy fuggveny fut'si idejet meri"""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        
        func(*args, *kwargs)
        
        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)
        
        print('Time is ', total_time, ' seconds')
    return wrapper

@get_time
def csinalsz(param: str):
    """Prints out a welcome text"""
    
    sleep(1)
    print(param)
    

if __name__ == '__main__':
    csinalsz('Good to see you!')
    print(csinalsz.__name__)
    print(csinalsz.__doc__)
    
        
        