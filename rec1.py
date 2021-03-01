#!/usr/bin/python3

import csv, urllib.request, os, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from em1 import var

url = 'https://thingspeak.com/channels/1104680/field/1.csv'
urllib.request.urlretrieve(url, var.csvLoc)
with open(var.csvLoc) as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		msg=row[2]
os.remove(var.csvLoc)
password_provided = input("Provide the key : ")
password = password_provided.encode()
key = base64.urlsafe_b64encode(var.kdf.derive(password))
f=Fernet(key)
print("\nEncrypted text you've received :\n\n"+msg)
msg=msg[2:-1]
msg=bytes(msg,'utf-8')
msg=f.decrypt(msg)
print("\nThe Message sent was: \n\n"+str(msg)[2:-1])