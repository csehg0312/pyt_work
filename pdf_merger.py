import PyPDF2
#import PyPDF4
import os

#path = "C:/Users/csehg/Documents/PÉNZÜGY"
path = input('Type the path to pdfs: ')
if os.path.exists(path):
    merger = PyPDF2.PdfMerger()
    #merge = PyPDF4.PdfFileMerger()

    for file in os.listdir(path):
        if file.endswith(".pdf"):
            print('Loading in... ', file)
            link = os.path.join(path,file)
            print(link)
            #print(vals)
            #vals.append(file)
            merger.append(link)
    print('Generating pdf...')
    name = input('Type a name: ')
    merger.write(f"{path}/{name}.pdf")

