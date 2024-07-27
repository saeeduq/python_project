#مشروع استخراج البيانات من موقع الويب 
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from datetime import datetime

def get_forecast_data():
    url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
                             'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

    response = requests.get(url, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        book_list = soup.find('ol', class_='row')

        book_titles = book_list.find_all('h3')
        titles = [book.find('a')['title'] for book in book_titles]

        whole_prices = soup.find_all('p', class_='price_color')
        prices = [price.contents[0] for price in whole_prices]
        data = list(zip(titles, prices)) 
        print(data)
        return data
    return None

def get_forecast_txt():
    data = get_forecast_data()
    if data:
        today = datetime.today().strftime('%Y-%m-%d')
        with open('titles_book.txt', 'w', encoding='utf-8') as f: 
            f.write('titles_book\n')
            f.write(today + '\n')
            f.write('='*24 + '\n')

            table = tabulate(data, headers=['titles', 'price'], tablefmt='psql')
            f.write(table)

if __name__ == '__main__':
    get_forecast_txt()
