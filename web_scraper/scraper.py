import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/MacBook_Pro"

page = requests.get(URL)

# print(page.content)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="mw-parser-output")

# print(results.prettify())

paragraph = results.find_all("sup")

print(paragraph)

def get_citations_needed_count():
    pass


def get_citations_needed_report():
    pass