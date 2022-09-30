import psutil

print('RAM memory % used', psutil.virtual_memory()[2])