from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import csv
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = request.get(url)
soup = bs(page,text,'html.parser')
star_table = soup.find_all('table')
table_row = star_table[7].find_all('te')
browser = webdriver.Chrome("C:/Users/user/Desktop/pycodes/Webscriping1/chromedriver_win32/chromedriver")
browser.get(start_url)
time.sleep(10)

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

def scrape():
    headers = []
    planet_data =[]
   for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7]

    Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []
            
    with open("scrapper1.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()


