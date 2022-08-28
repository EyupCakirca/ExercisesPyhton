import requests
from bs4 import BeautifulSoup
print("""
**************************************

IMDB TOP 250 FİLM GÖRÜNTÜLEME

**************************************
""")


url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")

değer = float(input("Kaç puan üzeri filmleri görüntülemek istiyorsunuz?: "))

titles = soup.find_all("td",{"class":"titleColumn"})
ranks = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for title,rank in zip(titles,ranks):
    title = title.text
    rank = rank.text

    title = title.strip()
    title = title.replace("\n","")

    rank = rank.strip()
    rank = rank.replace("\n","")

    if float(rank) > değer:
        print(title + " ---> " + rank)
