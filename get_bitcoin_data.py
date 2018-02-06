import pandas as pd
import requests
import csv
import json

START_DATE = '2010-07-17'
END_DATE = '2018-01-30'
URL = 'https://api.coindesk.com/v1/bpi/historical/close.json'

payload = {'start': START_DATE, 'end': END_DATE}
r = requests.get(URL, params=payload)
resp_dict = r.json()['bpi']

df = pd.DataFrame.from_dict(resp_dict, orient='index').sort_index()
df.columns = ['bpi']
df.to_csv('../data/bpi.csv')
