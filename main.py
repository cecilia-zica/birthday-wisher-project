import smtplib
import os
import datetime as dt
import random

MYEMAIL = os.environ.get("MYEMAIL")
PASSWORD = os.environ.get("PASSWORD")
#
# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
# connection.login(user= MYEMAIL, PASSWORD= PASSWORD)
# connection.sendmail(from_addr= MYEMAIL,
#                     to_addrs= "ceciliazica8789@gmail.com",
#                     msg="Hello\n\nThis is the body of the email.\n\nBest regards,\nCecilia Zica Camargo")
# connection.close()

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2004, month=12, day=11, hour=12)
# print(date_of_birth)

with open("quotes.txt") as quotes_file:
    all_quotes = quotes_file.readlines()

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week <= 4:
    random_quote = random.choice(all_quotes)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        connection.login(user= MYEMAIL, PASSWORD= PASSWORD)
        connection.sendmail(from_addr= MYEMAIL,
                            to_addrs= "ceciliazica8789@gmail.com",
                            msg=f"Subject:Let's have a good day!\n\n{random_quote}\n\nYou can do it, smile!")
        connection.close()