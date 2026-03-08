import requests
from bs4 import BeautifulSoup

def get_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2') # Thay đổi tag tùy trang web
    for i, title in enumerate(titles[:10]):
        print(f"{i+1}. {title.text.strip()}")

get_titles("https://news.ycombinator.com/")
