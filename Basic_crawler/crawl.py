import bs4 
from bs4 import BeautifulSoup as bs




url = "https://vnexpress.net/"
request = requests.get(url)
soup = bs(request.text,"html.parser")


Titles = soup.find_all("h3")

for title in Titles:
    try:
        #print(title.get_text());
        print(title.a.get("href"))
    except Exception as e:
        print(e)
        