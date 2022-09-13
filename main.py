import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69234177970014%2C%22north%22%3A37.85814816331502%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

headers = {
    "User-Agent": USER-AGENT,
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")

price_list = []
for price in soup.find_all(name="div", class_="kJFQQX"):
    price_list.append(price.getText()[:6])

link_list = []
for link in soup.find_all(name="div", class_="clrcsE"):
    new_link = link.find('a')["href"]
    if new_link[0] != 'h':
        new_link = "https://www.zillow.com" + new_link
    link_list.append(new_link)

address_list = []
for address in soup.find_all(name="div", class_="bDmKKM"):
    new_address = address.find('address').getText()
    address_list.append(new_address)

chrome_driver_path = "C:/Development/chromedriver.exe"
ser = Service(chrome_driver_path)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ser, options=chrome_options)

for i in range(len(price_list)):
    driver.get(SHEET_URL)
    time.sleep(2)

    answer_1 = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer_1.send_keys(address_list[i])

    answer_2 = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer_2.send_keys(price_list[i])

    answer_3 = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer_3.send_keys(link_list[i])

    submit_button = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()