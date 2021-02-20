#!/usr/bin/python3

#libraries
# for csv
import pandas as pandas
import io
# for email
import smtplib
from email.mime.text import MIMEText
from email.Header import Header


#classes
class var:
    csvLoc = '/home/users/slatino1/Git/ODU_Zoom_E2EE/mailing list.csv'
    csvName = "mailling list.csv"

#functions
def csv():
    # gather emails from csv file
    with open(csvName, "rU") as base_file:
        read_base_file = csv.reader(base_file, delimiter=",")
        duplicates_list = []
        rows = [row for row in read_base_file]
        for row in rows:
            duplicates_list.extend(row)









#references
#https://stackoverflow.com/questions/59253638/sending-an-email-with-python-using-csv-data-for-the-body
#   using csv file to get emails and then send the emails via panda