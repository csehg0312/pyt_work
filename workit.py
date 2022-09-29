import os 

working_directory = os.getcwd()

with os.scandir(working_directory) as entries:
    for entry in entries:
        print(entry.name)