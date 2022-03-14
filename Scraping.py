import requests
import bs4

url = "https://live.iticfoundation.org/#"
# url = "https://traffic.longdo.com/event"

res = requests.get(url)
res.encoding = 'utf-8'
res.raise_for_status()
html = res.text

soup = bs4.BeautifulSoup(html, "html.parser")
print(soup.prettify())