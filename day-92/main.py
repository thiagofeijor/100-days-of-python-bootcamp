import requests
from bs4 import BeautifulSoup

URL = "https://g1.globo.com/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

tag = soup.select('.feed-post-link')

all_news = [news.getText() for news in tag]

for new in all_news:
    print(new)
