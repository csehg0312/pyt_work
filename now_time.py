import datetime
while True:
    past = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    while True:
        nows = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        if(nows.strftime('%S') > past.strftime('%S')):
            print(nows)