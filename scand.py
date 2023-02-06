import os
from time import strftime
from datetime import datetime

path = 'C:/Users/csehg/Videos'

obj = os.scandir(path)

for file in obj:
    print(f'{file.name} --- {[os.path.getsize(file.path) if file.is_file()]} --- {file.is_dir()} --- {datetime.fromtimestamp((os.path.getmtime(file.path))).strftime("%Y/%B/%d (%A)")}')