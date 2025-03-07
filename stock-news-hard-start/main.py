import requests
from newsapi import NewsApiClient
from datetime import date
from datetime import timedelta
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = "ee31091ae44040f88f31b3772ajf7392"
stock_api_key = "RMT2PS9Z5123123213"
my_email = "denizhantest123@gmail.com"
password = "nalsvsdjnslkdfjslkdfj"


response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={stock_api_key}")
data = response.json()


today = date.today()
yesterday = str(today - timedelta(days=1))
before_yesterday = str(today - timedelta(days=2))

yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
before_yesterday_close = float(data["Time Series (Daily)"][before_yesterday]["4. close"])
percentage_diff = float((yesterday_close - before_yesterday_close) / yesterday_close)


if abs(percentage_diff) > 0.05: # greater than 5%
    # get top 3 news on the company
    newsapi = NewsApiClient(api_key=news_api_key)
    params = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": news_api_key,
        "language": "en",
    }
    response = requests.get(url="https://newsapi.org/v2/everything?", params=params)
    data = response.json()
    for n in range(3):
        news_title = str(data["articles"][n]["title"].encode("ascii", "ignore"))
        news_title = news_title[1:]
        news_content = str((data["articles"][n]["description"]).encode("ascii", "ignore"))
        news_content = news_content[1:]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="dodogep@gmail.com",
                                msg=f"Subject:{news_title}\n\n"
                                    f"{news_content}")