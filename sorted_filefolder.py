# def sorted_data(ut:str):
#     text_file_list = ['.txt','.rtf','.log', '.doc','.docx']
#     music_file_list = ['.mp3', '.mp4','.ma4','.flac','.wav','.wma']
#     pic_file_list = ['.jpg','.png','.tiff','.pdf','.gif', '.raw']
#     exec_file_list = ['.exe', '.msi']
#     zipped_file_list = ['.zip', '.7zip']
#     video_file_list = ['.mp4','.mov']
# 
#     #path = 'C:/Users/csehg/Documents'
#     filebase = {}
# 
#     def istxt(file:str):
#         _,comp = os.path.splitext(file)
#         if comp.lower() in text_file_list:
#             return 1
#         elif comp.lower() in music_file_list:
#             return 2
#         elif comp.lower() in pic_file_list:
#             return 3
#         elif comp.lower() in video_file_list:
#             return 4
#         elif comp.lower() in exec_file_list:
#             return 5
#         elif comp.lower() in zipped_file_list:
#             return 6
#         else:
#             return 0
#         
#     def getsize(path):
#         
#         return os.path.getsize(path)
# 
#     def getlasttime(path):
#         return os.path.getctime(path)
# 
# 
#         
# 
#     filebase.update({'Path':path})
#     parent, _ = os.path.split(path)
#     filebase.update({'Parent':parent})
#     print(filebase.values())
#     filebase.update({'Folders': deque([x for x in os.listdir(path) if os.path.isdir(os.path.join(path,x))])})
#     print(filebase.values())
#     print(sys.getsizeof(filebase))
#     # filebase.update({'Text Files:': [x for x in os.listdir(path) if istxt(x)]})
#     #filebase.update({'Files': deque([x for x in os.listdir(path) if os.path.isdir(os.path.join(path,x)) == False])})
#     # print(filebase.values())
#     # print(sys.getsizeof(filebase))
#     filebase.update({'Else': deque([x for x in os.listdir(path) if istxt(x) == 0 and x not in filebase.get('Folders')])})
#     filebase.update({'Text': deque([x for x in os.listdir(path) if istxt(x) == 1])})
#     filebase.update({'Music': deque([x for x in os.listdir(path) if istxt(x) == 2])})
#     filebase.update({'Photo': deque([x for x in os.listdir(path) if istxt(x) == 3])})
#     filebase.update({'Video': deque([x for x in os.listdir(path) if istxt(x) == 4])})
#     filebase.update({'Executables': deque([x for x in os.listdir(path) if istxt(x) == 5])})
#     filebase.update({'Zipped': deque([x for x in os.listdir(path) if istxt(x) == 6])})
#     print(filebase.items())