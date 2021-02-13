# https://medium.com/datadriveninvestor/end-to-end-encrypted-communication-using-python-a39d1c48a0fe
import csv
import urllib.request
import os
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
url = 'https://thingspeak.com/channels/1104680/field/1.csv'
urllib.request.urlretrieve(url, '/Users/YourName/Desktop/1.csv')
with open('1.csv') as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		msg=row[2]
os.remove('/Users/YourName/Desktop/1.csv')
password_provided = input("Provide the key : ")
password = password_provided.encode()
salt = b'salt_'
kdf = PBKDF2HMAC(
	algorithm=hashes.SHA256(),
	length=32,
	salt=salt,
	iterations=100000,
	backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f=Fernet(key)
print("\nEncrypted text you've received :\n\n"+msg)
msg=msg[2:-1]
msg=bytes(msg,'utf-8')
msg=f.decrypt(msg)
print("\nThe Message sent was: \n\n"+str(msg)[2:-1])
