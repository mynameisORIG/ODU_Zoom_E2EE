#!/usr/bin/python3

#make sure to do pip install urllib

# library
# for e2ee
import sys, urllib, urllib.request, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# our file we created
from email import csv

#variables
#change msg to emails
emails = 
msg=str(input('Enter your message : '))
password_provided = input("Provide a key : ")
password = password_provided.encode()
salt = b'salt_'
kdf = PBKDF2HMAC(
algorithm=hashes.SHA512(),
length=32,
salt=salt,
iterations=100000,
backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
urllib.request.urlopen
msg=msg.encode()
f = Fernet(key)
msg=f.encrypt(msg)
msg=str(msg)
#prints encrypted messaged
print("\nYour encrypted text is: "+msg)
b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=489HCQ5PQEJDRFUV&field1='+msg)
#success message
print("\nYour message has successfully been sent with end-to-end encryption!\nThe receiver needs to enter the same key.")
