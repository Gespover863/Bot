import requests
from bs4 import BeautifulSoup

from config import old_lots, new_lots, storage


async def search_lots():
    for url in storage:
        page = requests.get(url)

        soup = BeautifulSoup(page.text.encode('utf-8'), 'lxml')
        lots = soup.find_all(class_='cursor-pointer')

        if not lots:
            new_lots.append('У бота отвалилась жопа. Отпишись мне.')

        for lot in lots:
            lot_info = []

            for info in lot:
                try:
                    lot_info.append(info.text.replace('\r', '').replace('\n', '').split(' '))
                except:
                    continue

            for info in lot_info:
                while True:
                    try:
                        index = info.index('')
                        del info[index]

                    except ValueError:
                        break

            max_price = float(storage[url])
            price = float(lot_info[-2][0].replace(',', ''))

            if price <= max_price:
                data = ''

                for info in lot_info:
                    if info:
                        string = ' '.join(str(i) for i in info if i is not None)
                        data += string + '\n'

                if data not in old_lots:
                    new_lots.append(data)
                    old_lots.append(data)
