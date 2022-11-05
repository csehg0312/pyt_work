import shutil

total, used, free = shutil.disk_usage("/")

total = (total // (2**30))

if __name__ == '__main__':
    print('Total: %d GiB' % (total // (2**30)))
    print('Used: %d GiB' % (used // (2**30)))
    print('Free: %d GiB' % (free // (2**30)))