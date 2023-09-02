
#Mam you will have to change the to_dir and from_dir for the app to work!
import os
import shutil

from_dir = "C:/Users/troll/Downloads"

to_dir = "C:/Users/troll/document_files"

list_of_files = os.listdir(from_dir)
for i in list_of_files:
    name,extension = os.path.splitext(i)
    if extension == '':
        continue
    elif extension in ['.txt','.xlsx','.pptx','.docx','.xls','.ppt','.doc',]:
        path1 = from_dir+'/'+i
        path2 = to_dir+'/'+'document_files'
        path3 = to_dir+'/'+'document_files'+'/'+i
        if os.path.exists(path2):
            print("Moving " + name + "...")

            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + name + "...")
            shutil.move(path1,path3)
