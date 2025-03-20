import requests
from bs4 import BeautifulSoup
import os
import smtplib

URL = ("https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/dp/B0863TXGM3"
       "/ref=sr_1_3?crid=GIDGNAF6Y2X2&dib=eyJ2IjoiMSJ9.gk_i8PTSeTQwgA1HlpWXhtq6P7IpAYM9pJPZd"
       "KMHkCr7vynjvVXhliOVosvekFKaYMMqw-IdoS2RT4wdNHyeAqaP1hN7Ucfrac7sU6f8kxVw4IWQjJ0iSYCyP"
       "wba8ht_3wT4D2CaN_JW8asNluIh4lEyDyycP6EM0UFQfxzeWwN-vQ0QAqiSDOdefH2ips4Zebfqr26wSMbf9"
       "Dd42HCA2WsoCRBBopeX5vGc34ly0gE.hU-55Gl_JjdAWWgI9wcGUsDUUghJhFZdmdceZSlIe9Y&dib_tag=se"
       "&keywords=sony%2Bwh-1000xm4&qid=1742492927&sprefix=sony%2Bwh%2Caps%2C222&sr=8-3&th=1")

MY_EMAIL = os.environ["EMAIL_ENV"]
MY_PASSWORD = os.environ["PASSWORD_ENV"]

header = {"Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

response = requests.get(URL, headers=header)
instant_pot_web = response.text
soup = BeautifulSoup(instant_pot_web, "html.parser")

# Find the name of the product
product_name = soup.find(id="productTitle").getText().strip()
product_name = " ".join(product_name.split())

# Find the price of the product
price_whole = soup.find(name="span", class_="a-price-whole")
price_fraction = soup.find(name="span", class_="a-price-fraction")

price_str = price_whole.getText() + price_fraction.getText()
price = float(price_str)

BUY_PRICE = 200

print(soup.prettify())

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg="Subject: Amazon Low Price Alert\n\n"
                            f"{product_name} is now ${price}\n"
                            f"Shopping Link: {URL}".encode("utf-8"))
