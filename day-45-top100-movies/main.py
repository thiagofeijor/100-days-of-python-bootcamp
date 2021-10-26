import requests
import re
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.select('strong')

movie_titles = [movie.getText() for i, movie in enumerate(all_movies) if i % 2 == 0]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
