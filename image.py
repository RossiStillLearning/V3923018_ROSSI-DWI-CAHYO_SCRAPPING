import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('https://proxyway.com/news')
soup = BeautifulSoup(r.content, 'html.parser')

images_list = []
images = soup.select("img")

for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append((src, alt))

with open('images_info.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Src', 'Alt'])
    for image_info in images_list:
        writer.writerow([image_info[0], image_info[1]])

print("Data telah diekspor ke dalam file images_info.csv")
