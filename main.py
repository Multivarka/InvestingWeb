# from InvestingWeb.invest.models import ProductInvest
import requests
import apimoex
import time
import sqlite3


def get_items(title):
    conn = sqlite3.connect('InvestingWeb/db.sqlite3')
    cursor = conn.cursor()
    data = cursor.execute(f"SELECT * FROM invest_productinvest WHERE title='{title}'").fetchall()
    print(data)


get_items("")
# https://iss.moex.com/iss/securities.xml?q=EUR
def update_table():
    with requests.Session() as session:
        print(apimoex.get_index_tickers(session, 'moexbs'))
        # securities = [sec['SECID'] for sec in apimoex.get_index_tickers(session,'imoex')][:10]
        # for security in securities:
        #     data = apimoex.get_board_history(session, security)[-2:]
        #     volume1, value1 = data[-1]['VOLUME'], data[-1]['VALUE']
        #     volume2, value2 = data[0]['VOLUME'], data[0]['VALUE']
        #     if volume1 > 0:
        #         price = value1 / volume1
        #         if volume2 > 0:
        #             price2 = value2 / volume2
        #             perc = round((price - price2) / price2 * 100, 2)
        #             res = f'+{perc}%' if perc > 0 else f'{perc}%'
        #             # if not ProductInvest.objects.filter(title=security).exists():
        #             #     product = ProductInvest(title=security, price_now=round(price, 2), price_change=res)
        #             #     product.save()
        #             # else:
        #             #     product = ProductInvest.objects.get(title=security)
        #             #     product.price_now = round(price, 2)
        #             #     product.price_change = res
        #             #     product.save()
        #             print(f'{security} - {price}({res})')

# while True:
update_table()
    # time.sleep(10)