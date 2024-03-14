import os
from datasets import load_dataset

bbc_news_dataset = {}
for year in range(2017, 2024):
    for month in range(1, 13):
        date = str(year) + '-' + ('0' if month < 10 else '') + str(month)
        bbc_news_dataset[date] = load_dataset('RealTimeData/bbc_news_alltime', date)

#para comprobar correcta descarga
print(len(bbc_news_dataset['2017-01']['train']))
input()
