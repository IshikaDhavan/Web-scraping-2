from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

response = requests.get(START_URL)

if response.status_code == 200:
    soup= BeautifulSoup(response.text , "html.parser")
else:
     print("Failed to retrieve the page. Status code:", response.status_code)
     exit()


stars_data = []

def scrape():
    headers = ["proper_name","distance" , "mass" , "radius"]

    star_table = soup.find("table", {"class": "wikitable"})

    for row in star_table.find_all("tr")[1:]:
        columns = row.find_all("td")
        
        if len(columns) >= len(headers):
            temp_list = []
            for column in columns:
                if column.find("a") and len(temp_list) < len(headers):
                    temp_list.append(column.find("a").text.strip())
                elif len(temp_list) < len(headers):
                    temp_list.append(column.text.strip())
            
            # Append empty strings for any missing columns
            while len(temp_list) < len(headers):
                temp_list.append("")
            
            stars_data.append(temp_list)

    print(temp_list)
scrape()

headers = ["proper_name","distance" , "mass" , "radius"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(stars_data, columns=headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")

