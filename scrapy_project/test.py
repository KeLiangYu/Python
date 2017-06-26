# -*- coding: utf-8 -*-

import sqlite3
import numpy as np
import matplotlib.pyplot as pt

def disp_menu():
        print("世界天氣預報系統")
        print("------------------------")
        print("1.顯示天氣預報資訊")
        print("2.顯示月平均溫度圖(℃)")
        print("3.月平均雨量圖")
        print("0.結束")
        print("------------------------")

def disp_alldata():
    cursor = conn.execute('select * from test;')
    n = 0
    for row in cursor:
        print("地點：{}，天氣：{}，溫度(℃)：{}，最低月平均溫度(℃)：{}，最高月平均溫度(℃)：{}，月平均雨量(毫米)：{}，月平均雨量(>=0.1毫米日數)：{}". \
            format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        n = n + 1
        if n == 20:
            x = input("請按Enter鍵繼續...(Q:回主選單)")
            if x == 'Q' or x == 'q': break
            n = 0

def average_temperature():
    print("1.顯示月平均溫度圖(℃) - 最低")
    print("2.顯示月平均溫度圖(℃) - 最高")
    choice = int(input("請輸入您的選擇："))
    data = []
    city = list()
    temperature = list()
    cursor = conn.execute('select * from test;')
    for row in cursor:
        data.append(list(row))
    if choice == 1 :
        for p in data[0:10]:
            city.append(p[0])
            temperature.append(p[3])
            ind = np.arange(len(city))
    else :
        for p in data[0:10]:
            city.append(p[0])
            temperature.append(p[4])
            ind = np.arange(len(city))
    pt.bar(ind, temperature)
    pt.xticks(ind+0.5, city)
    pt.title('顯示月平均溫度(℃)')
    pt.show()

def average_rainfall():
    print("1.顯示月平均雨量圖 - 毫米")
    print("2.顯示月平均雨量圖 - >=0.1毫米日數")
    choice = int(input("請輸入您的選擇："))
    data = []
    city = list()
    rainfall = list()
    cursor = conn.execute('select * from test;')
    for row in cursor:
        data.append(list(row))
    if choice == 1 :
        for p in data[0:10]:
            city.append(p[0])
            rainfall.append(p[5])
            ind = np.arange(len(city))
    else :
        for p in data[0:10]:
            city.append(p[0])
            rainfall.append(p[6])
            ind = np.arange(len(city))
    pt.bar(ind, rainfall)
    pt.xticks(ind+0.5, city)
    pt.title('顯示月平均雨量圖')
    pt.show()

conn = sqlite3.connect('test.sqlite')

while True:
    disp_menu()
    choice = int(input("請輸入您的選擇："))
    if choice == 0 : 
        conn.close()
        break
    if choice == 1 :
        disp_alldata()
    elif choice == 2:
        average_temperature()
    elif choice == 3:
        average_rainfall()
    else: break
    x = input("請按Enter鍵回主選單")
        