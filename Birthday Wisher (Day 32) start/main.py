"""
import smtplib

my_email = "denizhantest123@gmail.com"
password = "nals vwgv neeb hzjd"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="denizhantest123@yahoo.com",
                        msg="Subject:Hello\n\n"
                            "This is the body of my email")
"""

"""
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1764, month=5, day=31, hour=3)
print(date_of_birth)
"""

import datetime as dt
import random
import smtplib

my_email = "denizhantest123@gmail.com"
password = "abcd abcd nvkw jues"
beyz_email = "test123_s@hotmail.com"

now = dt.datetime.now()
current_day = now.weekday()

# Random quote
def random_quote():
    quote = random.choice(all_quotes)
    return quote

if current_day == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
    random_quote = random_quote()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=beyz_email,
                            msg="Subject: Motivational Quote\n\n"
                                f"{random_quote}")