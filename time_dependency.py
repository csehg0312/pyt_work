import datetime

def time_mod(time, delta, epoch=None):
    if epoch is None:
        epoch = datetime.datetime(1970, 1, 1, tzinfo=time.tzinfo)
    return (time - epoch) % delta

def time_round(time, delta, epoch=None):
    mod = time_mod(time, delta, epoch)
    
    return time - mod
    #return time + (delta - mod)

def time_floor(time, delta, epoch=None):
    mod = time_mod(time, delta, epoch)
    return time - mod

def time_ceil(time, delta, epoch=None):
    mod = time_mod(time, delta, epoch)
    if mod:
        return time + (delta - mod)
    return time

def called(CT):
    CTV = time_round(CT, datetime.timedelta(seconds=5))
    return CTV

if __name__ == '__main__':
    tim = datetime.datetime(2022,5,9, 6,39,55,55848)
    print(time_round(tim, datetime.timedelta(seconds=1)))