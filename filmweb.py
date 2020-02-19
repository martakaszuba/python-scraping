from urllib import request
from bs4 import BeautifulSoup as bs

fl = open("C:\\Users\\Marta\\Desktop\\Python\\scraping\\filmweb.txt", "a")
for i in range(1,10):
    if i ==1:
        req = request.urlopen("".join(["https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page=1"]))
    else :
        req = request.urlopen("".join(["https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page="+str(i)]))
    raw_html = req.read()
    soup = bs(raw_html, "html.parser")
    titles = soup.find_all("h3", class_="filmPreview__title")
    rates = soup.find_all("span", class_="rateBox__rate")
    counts = soup.find_all("span",class_="rateBox__votes rateBox__votes--count")
    directors = soup.find_all("div",class_="filmPreview__info filmPreview__info--directors")
    for i,x in enumerate(titles):
        titles[i]= "".join(list(titles[i].strings))
    for i,x in enumerate(rates):
        rates[i]= "".join(list(rates[i].strings))
    for i,x in enumerate(counts):
        counts[i]= "".join(list(counts[i].strings))
    for i,x in enumerate(directors):
        directors[i]= "".join(list(directors[i].strings))
        directors[i] =directors[i].replace("reżyser", "")
    for i,x in enumerate(titles):
        fl.write(titles[i]+"|"+rates[i]+"|"+counts[i]+"|"+directors[i]+"\n")
fl.close()
