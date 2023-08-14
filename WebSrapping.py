import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
page = requests.get(
    "https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome..69i57j0i433i512j0i67i650j0i131i433i512j0i67i650j0i433i512l5.3740j0j7&sourceid=chrome&ie=UTF-8", headers=headers)  # acessa a página


# transforma em um objeto para que possamos fazer o nosso web scrapping
soup = BeautifulSoup(page.content, 'html.parser')

valor_dolar = soup.find_all("span", class_="DFlfde SwHCTb")[0]

print(f"O valor do dolár no momento é {valor_dolar.text}")
