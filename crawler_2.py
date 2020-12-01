import bs4
from bs4 import BeautifulSoup as bs
import selenium
from selenium import webdriver

def get_page(url):
    driver = webdriver.Chrome(executable_path= "C:\Program Files\Google\chromedriver.exe")
    driver.set_window_position(-10000,0)
    driver.get(url)
    body = driver.page_source
    driver.close()
    soup = bs(body,"html.parser")
    return soup.prettify()
urls =[ "https://Zing.vn","https://dantri.vn","https://nhandan.vn","https://thanhnien.vn"]
for url in urls :
    get_page(url)
