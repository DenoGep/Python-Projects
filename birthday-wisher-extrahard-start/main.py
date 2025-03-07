##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv DONE

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import random
import pandas
import smtplib

PLACEHOLDER = "[NAME]"
my_email = "denizhantest123@gmail.com"
password = "nals abcd abcd abcd"


now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        letter = letter_file.read()
        final_letter = letter.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                                msg="Subject: Happy Birthday\n\n"
                                    f"{final_letter}")