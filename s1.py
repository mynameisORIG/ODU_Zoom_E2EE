#!/usr/bin/python3

import sys, urllib, urllib.request, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from em1 import var

msg=str(input('Enter your message : '))
password_provided = input("Provide a key : ")
password = password_provided.encode()

key = base64.urlsafe_b64encode(var.kdf.derive(password))
urllib.request.urlopen
msg=msg.encode()
f = Fernet(key)
msg=f.encrypt(msg)
msg=str(msg)
print("\nYour encrypted text is: "+msg)
b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=489HCQ5PQEJDRFUV&field1='+msg)
print("\nYour message has successfully been sent with end-to-end encryption!\nThe receiver needs to enter the same key.")

# https://medium.datadriveninvestor.com/end-to-end-encrypted-communication-using-python-a39d1c48a0fe