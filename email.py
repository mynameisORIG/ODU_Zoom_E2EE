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
    sender_email = "mymail@gmail.com"
    receiver_email = "anothermail@gmail.com"
    password = "mypass"

#functions
def csv():
    # gather emails from csv file
    with open(csvName, "rU") as base_file:
        read_base_file = csv.reader(base_file, delimiter=",")
        duplicates_list = []
        rows = [row for row in read_base_file]
        for row in rows:
            duplicates_list.extend(row)

str_io = io.StringIO()
df = pd.read_csv(var.csvLoc)
df.to_html(buf=str_io)
table_html = str_io.getvalue()
print(table_html)


message = MIMEMultipart("alternative")
message["Subject"] = "Subject: Your Title"
message["From"] = var.sender_email
message["To"] = var.receiver_email

text = """\
Subject: Your Title"""

html = """\
<html>
  <body>
    <p>{table_html}</p>
  </body>
</html>
""".format(table_html=table_html)

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# Send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(var.sender_email, var.password)
    server.sendmail(
        var.sender_email, var.receiver_email, message.as_string()
    )








#references
#https://stackoverflow.com/questions/59253638/sending-an-email-with-python-using-csv-data-for-the-body
#   using csv file to get emails and then send the emails via panda