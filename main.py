import requests
from bs4 import BeautifulSoup

URL = "https://www.businessinsider.com/50-best-movies-all-time-critics-2016-10?IR=T#50-children-of-paradise-1945-1"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h2", class_="slide-title-text")
movie_title = [movie.getText() for movie in all_movies]
movies_ordered = movie_title[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies_ordered:
        file.write(f"{movie}\n")