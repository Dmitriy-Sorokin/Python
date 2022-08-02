import zipfile
import os

folder_path = 'c:\\local git reposiroty\\Python\\folder'
zip_path = 'c:\\local git reposiroty\\Python\\folder\\test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

# my_zip.write('c:\\local git reposiroty\\Python\\folder\\1.', compress_type=zipfile.ZIP_DEFLATED)

for folder, files in os.walk(folder_path):
    print(folder, files)
    for file in files:
        my_zip.write(os.path.join(folder, files), file, compress_type=zipfile.ZIP_DEFLATED )

my_zip.close()