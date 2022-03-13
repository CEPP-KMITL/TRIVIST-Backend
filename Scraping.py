import requests
import bs4

url = "https://live.iticfoundation.org/#"

res = requests.get(url, timeout=(3.05, 27))
res.encoding = 'utf-8'
res.raise_for_status()
html = res.text

soup = bs4.BeautifulSoup(html, "lxml")
print(soup.text)