from constants import alphaKey
from pandasql import sqldf
from io import StringIO
import pandas as pd
import requests


class StocksApi:

    @staticmethod
    def runApi(stocks):
        """

        :param stocks:
        :return:
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=' \
              f'{stocks}&apikey={alphaKey}&datatype=csv'
        r = requests.get(url)

        df = pd.read_csv(StringIO(r.text))

        return df

    def selectWallets(self, stocksList):
        """

        :param stocksList:
        :return:
        """

        for stocks in stocksList:
            data =

        return recomendation
