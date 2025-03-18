import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movie_names = []
for movie in movies:
    name = movie.getText()
    movie_names.append(name)
movie_names.reverse()

with open('movies.txt', mode='w', encoding="utf-8") as file:
    for movie in movie_names:
        file.write(f"{movie}\n")


