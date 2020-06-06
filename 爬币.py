#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:38:02 2020

@author: johnson7days
"""



import requests,openpyxl,json
from bs4 import BeautifulSoup

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='币种'
sheet['A1']='币种(按市值排名)'
sheet['B1']='总市值(usd)'
sheet['C1']='U最高价'
sheet['D1']='U最高价历史时间'
sheet['E1']='U最低价'
sheet['F1']='U最低价历史时间'
sheet['G1']='备注'
url1='https://dncapi.bqiapp.com/api/coin/web-coinrank?'


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

for x in range(2):
    params={
        
        
        'page': str(x+1),
        'type':'-1',
        'pagesize':'100',
        'webp':'1'
        
        }
    
    res_coin=requests.get(url1,headers=headers,params=params)
    json_coin=json.loads(res_coin.text)
    
    
    list_coins=json_coin['data']


    for coin in list_coins:
        name=coin['fullname']
        c_value=coin['market_value_usd']
        high_price=coin['high_price']
        high_time=coin['high_time']
        low_price=coin['low_price']
        low_time=coin['low_time']
        coincode=coin['name']
        sheet.append([name,c_value,high_price,high_time,low_price,low_time,coincode])
    

wb.save('coin0020.xlsx')
    