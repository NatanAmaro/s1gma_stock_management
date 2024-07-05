from constants import alphaKey
from io import StringIO
import pandas as pd
import requests


def main(stocks):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=' \
          f'{stocks}&apikey={alphaKey}&datatype=csv'
    r = requests.get(url)

    df = pd.read_csv(StringIO(r.text))

    return df
