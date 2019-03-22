'''
Open Directory Link Scraper
by HarshanaS (http://github.com/harshanas)
---------------------------------------
Allows you to scrape links from an open Directory of your choice to a text File.

Use Cases:
+ Can be used to Scrape Links to the text file and import into IDM
+ Can be used in File Upload sites which allow multiple uploads

Usage:
python Main.py https://nodejs.org/dist/
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys


def scrape(url):
    links = []
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    ahrefs = soup.find_all("a")
    for a in ahrefs:
        links.append(page.url + a.attrs['href'])
    links = "\n".join(links)
    file = open("Links.txt","w")
    file.write(links)
    file.close()
    print("Links are written to Links.txt File")


if __name__ == "__main__":
    url = sys.argv[1]
    scrape(url)
