# a simple program to make love files
# cool file name huh :)
import zipfile
import os
import shutil

print('what the heck is going on here')

saveTo = ''
outputName = 'noProb'
directory = 'test'

def zipAll(directory, outputName):
    with zipfile.ZipFile(outputName, 'w') as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Add the file to the zip, preserving the directory structure
                arcname = os.path.relpath(file_path, start=directory)
                zipf.write(file_path, arcname)
    print("zipped the shit :)")

zipAll(directory,outputName)

def rename():
	shutil.move(outputName,outputName+'.love')

rename()