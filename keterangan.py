import requests
from bs4 import BeautifulSoup
import csv

url = 'https://proxyway.com/news'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    div_elements = soup.find_all('div', attrs={'data-widget_type': 'theme-post-excerpt.default'})

    if div_elements:
        
        with open('keterangan.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)

            for div_element in div_elements:
                inner_div = div_element.find('div', class_='elementor-widget-container')
                if inner_div:
                    text_content = inner_div.get_text(strip=True)
                    csvwriter.writerow([text_content])
                    print(text_content)
else:
    print(f'Failed to fetch webpage. Status code: {response.status_code}')