# a simple program to make love files
# cool file name huh :)
import zipfile
import os

print('what the heck is going on here')

def zipAll(directory, outputName):
    with zipfile.ZipFile(output_filename, 'w') as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Add the file to the zip, preserving the directory structure
                arcname = os.path.relpath(file_path, start=source_dir)
                zipf.write(file_path, arcname)
    print("zipped the shit :)")
