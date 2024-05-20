import requests
from bs4 import BeautifulSoup
import csv

url = 'https://proxyway.com/news'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all('h2')
    data = []
    
    for title in titles:
        data.append(title.text)

    with open('titles.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])
        writer.writerows(map(lambda x: [x], data))

    print("Data telah diekspor ke dalam file titles.csv")
else:
    print('Gagal mengambil halaman:', response.status_code)
