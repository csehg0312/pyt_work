
lis = [['3.feladat.pl', '271 b', '2022-01-15 21:10:10', '.pl'], ['4.feladat', ' ', ' ', 'directory'], ['5.feladat', ' ', ' ', 'directory'], ['7.feladat', ' ', ' ', 'directory'], ['8.feladat.pl', '1.33 kb', '2022-01-15 21:14:15', '.pl'], ['eredmeny.txt', '0 b', '2022-01-02 18:46:30', '.txt'], ['fordito.pl', '437 b', '2022-01-05 12:17:40', '.pl'], ['fordito02.pl', '1.31 kb', '2022-01-15 13:56:00', '.pl'], ['gorog.txt', '659 b', '2022-01-05 12:14:50', '.txt'], ['gorog2.txt', '616 b', '2022-01-05 12:24:40', '.txt'], ['guessnum.pl', '998 b', '2022-01-08 21:04:55', '.pl'], ['gyakorol.pl', '1.56 kb', '2022-01-16 11:41:50', '.pl'], ['index01.html', '1.13 kb', '2022-01-16 11:32:00', '.html'], ['index2.html', '1.15 kb', '2022-01-16 11:20:40', '.html'], ['index3.html', '66.08 kb', '2022-01-20 09:50:10', '.html'], ['indexcsere.pl', '1.16 kb', '2022-01-08 14:28:05', '.pl'], ['indexcsere01.pl', '2.35 kb', '2022-01-08 15:06:50', '.pl'], ['kolak.pl', '2.71 kb', '2022-01-17 18:35:30', '.pl'], ['norhun.txt', '123 b', '2022-01-16 11:40:15', '.txt'], ['program.pl', '275 b', '2022-01-02 18:39:25', '.pl'], ['program02.pl', '113 b', '2022-01-05 15:00:00', '.pl'], ['russ.txt', '3.91 kb', '2022-01-15 13:53:55', '.txt'], ['russ0001.txt', '3.95 kb', '2022-01-16 12:27:50', '.txt'], ['russ0002.txt', '3.02 kb', '2022-01-16 12:28:05', '.txt'], ['russ001.txt', '3.07 kb', '2022-01-16 12:18:10', '.txt'], ['russ002.txt', '2.43 kb', '2022-01-16 12:18:30', '.txt'], ['russ01.txt', '3.96 kb', '2022-01-16 12:06:00', '.txt'], ['russ02.txt', '2.82 kb', '2022-01-16 12:07:10', '.txt'], ['russ2.txt', '2.84 kb', '2022-01-15 14:23:45', '.txt'], ['russ3.txt', '2.85 kb', '2022-01-15 14:30:35', '.txt'], ['segitseg01.pl', '1.83 kb', '2022-01-02 18:49:10', '.pl'], ['segitseg02.pl', '411 b', '2022-01-02 19:58:30', '.pl'], ['segitseg03.pl', '483 b', '2022-01-02 20:23:20', '.pl'], ['szavak.pl', '414 b', '2022-02-03 22:39:55', '.pl'], ['szoveg.txt', '5.87 kb', '2022-01-02 18:08:50', '.txt'], ['theformula.txt', '24 b', '2022-02-06 13:01:45', '.txt']]


def modify_list(LST:list, lngth:int):
    for l in range(4):
        for k in range(lngth):
            LST[k].pop()
    return LST

if __name__ == '__main__':
    print(len(lis))
    valaf = modify_list(lis,len(lis))
    print(str(valaf))
