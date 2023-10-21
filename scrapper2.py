from bs4 import BeautifulSoup as bd
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

response = requests.get(url)

soup = bd(response.text , 'html.parser')

star_table = soup.find_all('table')

temp_list = []

table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    if td is not None:
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)



Star_names = []
Distance = []
Mass = []
Radius = []


for i in range(1,len(temp_list)):

    if len(temp_list) >= 9:

        Star_names.append(temp_list[i][0])
        Distance.append(temp_list[i][5])
        Mass.append(temp_list[i][7])
        Radius.append(temp_list[i][8])

df_2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)), columns= ('Star_name','Distance','Mass','Radius'))
print(df_2)

df_2.to_csv('Brown Dawrf Stars.csv')