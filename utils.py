from requests import get
from requests.exceptions import ConnectionError
from common import API_KEY
import json

# ticker = 'IBM'

RESOURSE = f'https://www.alphavantage.co/query?apikey={API_KEY}'


# hardcoded for now
TICKER = 'MSFT'
FUNC = 'TIME_SERIES_INTRADAY'


def ping_url(url):
    try:
        r = get(url)
        return (True, r.json())
    except ConnectionError:
        return False

def url_builder(ticker, func):
    resourse = RESOURSE.split('?')
    return resourse[0] + f'?function={func}&' + \
        f'symbol={ticker}&' + 'interval=5min&' + 'outputsize=compact&' + resourse[1]


def fetch_info_by_ticker(ticker, func):
    request = url_builder(ticker, func)
    print(request)
    check = ping_url(request)
    if check:
        return check[1]
    raise ValueError("Failed to retrieve data from Alpha Vantage API.")


def parse_data():
    data = fetch_info_by_ticker(TICKER, FUNC)
    print(data)
    # print(data['Time Series (5min)'])


parse_data()

# fetch_info_by_ticker(TICKER, FUNC)