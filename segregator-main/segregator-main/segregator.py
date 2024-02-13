import os
import shutil
fromdir="C:\Users\HP\Desktop\python\c103"
todir="C:\Users\HP\Desktop\python\c103etc"
listOfFiles=os.listdir(fromdir)
for fileName in listOfFiles:
    name,extention=os.path.splitext(fileName)
    if extention == '':
        continue
    if extention in ['.pptx,docx,.doc,.pdf,.txt.ppt']  :
        path1=fromdir+'/'+fileName
        path2=todir+'/'+"documents"
        path3=todir+'/'+'documents'+'/'+fileName
        if os.path.exists(path2)   :
            print("moving "+fileName)
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("moving "+fileName)
            shutil.move(path1,path3)