import requests
from twilio.rest import Client
import os
import smtplib

MY_LAT = 40.982270
MY_LONG = 29.108890
api_key = "92070e701f6c63efaa2c3468hhh182"
account_sid = "AC84e057a8669f9b5e571829ssskc29124"
auth_token = "89b7956e5963233870eef3ui12orfo2"
my_email = "test12@gmail.com"
password = "dfjkdnflgksjdflksdjflsıdkj"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
def going_to_rain():
    for n in range(parameters["cnt"]):
        weather_id = weather_data["list"][n]["weather"][0]["id"]
        if weather_id < 700:
            global will_rain
            will_rain = True

going_to_rain()

# Twilio doesn't send SMS to Turkey but it's the sending code below
"""
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+13142624961', # Twilio trial SMS number
        to='+905445907056' # Your number
    )
    print(message.status)
"""

mail_list = ["test123@gmail.com", "test1234@gmail.com", "test12345@gmail.com"]
# Sending email
if will_rain:
    for mail in range(len(mail_list)):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=mail_list[mail],
                                msg="Subject: Rain Today!\n\n"
                                    "It's going to rain today. Remember to bring an umbrella.")