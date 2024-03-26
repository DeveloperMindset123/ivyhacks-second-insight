import step2
import requests
import json
import datetime
import time

#file that contains all the neccessary api calls and their apropriate responses, and their output is saved within the Data directory



stock_ticker = step2.stock_ticker
start_date = step2.start_date   # modify this value as needed
end_date = step2.end_date

print(stock_ticker)

def aggregateBars():
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&limit=120&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"

    response = requests.get(url)
    print("\nGet the aggregate bars for a stock symbol in a given time range in custom time window size:")
    print(response.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/aggregate-bars.json', 'w') as file:
        json.dump(json.loads(response.content), file, indent=4)

aggregateBars()


def dailyOpenHighLowCloseVolume():
    url2 = f"https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{start_date}?adjusted=true&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the daily open, high, low, and close(OHLC) for the entire stocks/equities market")
    response2 = requests.get(url2)
    print(response2.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/grouped-daily.json', 'w') as file:
        json.dump(json.loads(response2.content), file, indent=4)

dailyOpenHighLowCloseVolume()
#time.sleep(20)  # sleep for 62 seconds before continuing

"""
#get the daily open, high, low, close, and volume data 
url2 = f"https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{start_date}?adjusted=true&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nGet the daily open, high, low, and close(OHLC) for the entire stocks/equities market")
response2 = requests.get(url2)
print(response2.content)
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/grouped-daily.json', 'w') as file:
    json.dump(json.loads(response2.content), file, indent=4) """
        
def openClose():
    url3 = f"https://api.polygon.io/v1/open-close/{stock_ticker}/{start_date}?adjusted=true&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the open, close and afterhours prices of a stock symbol on a certain date:")
    response3 = requests.get(url3)
    print(response3.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/open-close.json', 'w') as file:
        json.dump(json.loads(response3.content), file, indent=4)

openClose()

"""

#get the open,close and afterhours prices of a stock symbol on a certain date
url3 = f"https://api.polygon.io/v1/open-close/{stock_ticker}/{start_date}?adjusted=true&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nGet the open, close and afterhours prices of a stock symbol on a certain date:")
response3 = requests.get(url3)
print(response3.content)
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/open-close.json', 'w') as file:
    json.dump(json.loads(response3.content), file, indent=4) """

def previousClose():
    url4 = f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/prev?adjusted=true&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nOn the previous day's open, high,low and close (OHLC) for the specified stock ticker:")
    response4 = requests.get(url4)
    print(response4.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/previous-close.json', 'w') as file:
        json.dump(json.loads(response4.content), file, indent=4)

previousClose()
#time.sleep(20)  # sleep for 62 seconds before continuing

"""
url4 = f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/prev?adjusted=true&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nOn the previous day's open, high,low and close (OHLC) for the specified stock ticker:")
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/previous-close.json', 'w') as file:
    response4 = requests.get(url4)
    print(response4.content) """

'''  --> 3 api calls listed below requires a subscription to the Polygon API
#get trades for a ticker symbol in a given time range
url5 = f"https://api.polygon.io/v3/trades/{stock_ticker}?{start_date}&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nGet trades for a ticker symbol in a given time range:")
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/trades.json', 'w') as file:
    response5 = requests.get(url5)
    print(response5.content)

url6 = f"https://api.polygon.io/v2/last/trade/{stock_ticker}?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nGet the most recent trade for a given stock:")
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/last-trade.json', 'w') as file:
    response6 = requests.get(url6) 
    print(response6.content)



url7 = f"https://api.polygon.io/v3/quotes/AAPL?timestamp={datetime.datetime.now().strftime("%Y-%m-%d")}&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nGet the most recent quote for a given stock: (realtime)")  
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/getQuote.json', 'w') as file:
    response7 = requests.get(url7) 
    print(response7.content)
'''

def simpleMovingAverage():
    url5 = f"https://api.polygon.io/v1/indicators/sma/{stock_ticker}?timespan=day&adjusted=true&window=50&series_type=close&order=desc&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the simple moving average(SMA) for a stock symbol over a given time range:")
    response5 = requests.get(url5)
    print(response5.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/sma.json', 'w') as file:
        json.dump(json.loads(response5.content), file, indent=4)

simpleMovingAverage()

"""
url5 = f"https://api.polygon.io/v1/indicators/sma/{stock_ticker}?timespan=day&adjusted=true&window=50&series_type=close&order=desc&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nGet the simple moving average(SMA) for a stock symbol over a given time range:")
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/sma.json', 'w') as file:
    response5 = requests.get(url5)
    print(response5.content)
"""

def exponentialMovingAverage():
    url6 = f"https://api.polygon.io/v1/indicators/ema/{stock_ticker}?timespan=day&adjusted=true&window=50&series_type=close&order=desc&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the exponential moving average (EMA) for a ticker symbol over a given day:")
    response6 = requests.get(url6)
    print(response6.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/ema.json', 'w') as file:
        json.dump(json.loads(response6.content), file, indent=4)

exponentialMovingAverage()
#time.sleep(20)  # sleep for 62 seconds before continuing

"""
url6 = f"https://api.polygon.io/v1/indicators/ema/{stock_ticker}?timespan=day&adjusted=true&window=50&series_type=close&order=desc&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nGet the exponential moving average (EMA) for a ticker symbol over a given day:")
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/ema.json', 'w') as file:
    response6 = requests.get(url6)
    print(response6.content)  """

def movingAverageConvergenceDivergence():
    url7= f"https://api.polygon.io/v1/indicators/macd/{stock_ticker}?timespan=day&adjusted=true&short_window=12&long_window=26&signal_window=9&series_type=close&expand_underlying=true&order=desc&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet moving average convergence divergence (MACD) for a stock symbol over a given time range:")
    response7 = requests.get(url7)
    print(response7.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/macd.json', 'w') as file:
        json.dump(json.loads(response7.content), file, indent=4)

movingAverageConvergenceDivergence()
    

"""

url7= f"https://api.polygon.io/v1/indicators/macd/{stock_ticker}?timespan=day&adjusted=true&short_window=12&long_window=26&signal_window=9&series_type=close&expand_underlying=true&order=desc&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nGet moving average convergence divergence (MACD) for a stock symbol over a given time range:")
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/macd.json', 'w') as file:
    response7 = requests.get(url7)
    print(response7.content) """

def relativeStrengthIndex():
    url8 = f"https://api.polygon.io/v1/indicators/rsi/{stock_ticker}?timespan=day&adjusted=true&window=14&series_type=close&order=desc&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the relative strength index (RSI) for a stock symbol over a given time range:")
    response8 = requests.get(url8)
    print(response8.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/rsi.json', 'w') as file:
        json.dump(json.loads(response8.content), file, indent=4)

relativeStrengthIndex()


"""
url8 = f"https://api.polygon.io/v1/indicators/rsi/{stock_ticker}?timespan=day&adjusted=true&window=14&series_type=close&order=desc&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nGet the relative strength index (RSI) for a stock symbol over a given time range:")
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/rsi.json', 'w') as file:
    response8 = requests.get(url8)
    print(response8.content) """


def tickerSymbols():
    url9 = f"https://api.polygon.io/v3/reference/tickers?ticker={stock_ticker}&active=true&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nQuery all ticker symbols which are supported by Polygon.io. This API currently includes Stocks/Equities, Crypto, and Forex pairs:")
    response9 = requests.get(url9)
    print(response9.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/tickers.json', 'w') as file:
        json.dump(json.loads(response9.content), file, indent=4)

tickerSymbols()
#time.sleep(20)  # sleep for 62 seconds before continuing

"""
url9 = f"https://api.polygon.io/v3/reference/tickers?ticker={stock_ticker}&active=true&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\nQuery all ticker symbols which are supported by Polygon.io. This API currently includes Stocks/Equities, Crypto, and Forex pairs:")
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/tickers.json', 'w') as file:
    response9 = requests.get(url9)
    print(response9.content)    """


def tickerDetails():
    url10 = f"https://api.polygon.io/v3/reference/tickers/{stock_ticker}?date={datetime.datetime.now().strftime("%Y-%m-%d")}4&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\n Get a single ticker's details by its ticker symbol:")
    response10 = requests.get(url10)
    print(response10.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/ticker-details.json', 'w') as file:
        json.dump(json.loads(response10.content), file, indent=4)
    
tickerDetails()

#time.sleep(62)  # sleep for 62 seconds before continuing

"""
# ticker details
url10 = f"https://api.polygon.io/v3/reference/tickers/{stock_ticker}?date={datetime.datetime.now().strftime("%Y-%m-%d")}4&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
print("\n Get a single ticker's details by its ticker symbol:")
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/ticker-details.json', 'w') as file:
    response10 = requests.get(url10)
    print(response10.content)
 """


def allNews():
    url11 = f"https://api.polygon.io/v2/reference/news?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the latest news for all stocks:")
    response11 = requests.get(url11)
    print(response11.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/Allnews.json', 'w') as file:
        json.dump(json.loads(response11.content), file, indent=4)   

allNews()
"""
url11 = f"https://api.polygon.io/v2/reference/news?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  #get the latest news for all stocks
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/Allnews.json', 'w') as file:
    response11 = requests.get(url11)
    print(response11.content)
"""

def specificStockNews():
    url12 = f"https://api.polygon.io/v2/reference/news?ticker={stock_ticker}&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the latest news for a specific stock:")
    response12 = requests.get(url12)
    print(response12.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/SpecificStockNews.json', 'w') as file:
        json.dump(json.loads(response12.content), file, indent=4)

specificStockNews()
"""
url12 = f"https://api.polygon.io/v2/reference/news?ticker={stock_ticker}&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  # get the latest news for a specific stock
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/SpecificStockNews.json', 'w') as file:
    response12 = requests.get(url12)
    print(response12.content) """


def marketHolidays():
    url13 = f"https://api.polygon.io/v1/marketstatus/upcoming?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the upcoming makret holidays and their closed times")
    response13 = requests.get(url13)
    print(response13.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/MarketHolidays.json', 'w') as file:
        json.dump(json.loads(response13.content), file, indent=4)

marketHolidays()
#time.sleep(20)  # sleep for 62 seconds before continuing

"""
url13 = f"https://api.polygon.io/v1/marketstatus/upcoming?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  # get the upcoming makret holidays and their closed times#
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/MarketHolidays.json', 'w') as file:
    response13 = requests.get(url13)
    print(response13.content)
"""

def marketStatus():
    url14 = f"https://api.polygon.io/v1/marketstatus/now?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the current trading status of the exchanges and overall financial markets")
    response14 = requests.get(url14)
    print(response14.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/MarketStatus.json', 'w') as file:
        json.dump(json.loads(response14.content), file, indent=4)

marketStatus()
#time.sleep(20)  # sleep for 62 seconds before continuing

"""
url14 = f"https://api.polygon.io/v1/marketstatus/now?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  #get the current trading status of the exchanges and overall financial markets
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/MarketStatus.json', 'w') as file:
    response14 = requests.get(url14)
    print(response14.content)  """


def stockSplitList():
    url15 = f"https://api.polygon.io/v3/reference/splits?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  # get a list of histocial splits, including the ticker symbol, the execution date, and the factors of the split ratio
    print("\nGet a list of historical splits, including the ticker symbol, the execution date, and the factors of the split ratio")
    response15 = requests.get(url15)
    print(response15.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/SplitList.json', 'w') as file:
        json.dump(json.loads(response15.content), file, indent=4)

stockSplitList()

"""
url15 = f"https://api.polygon.io/v3/reference/splits?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  # get a list of histocial splits, including the ticker symbol, the execution date, and the factors of the split ratio
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/SplitList.json', 'w') as file:
    response15 = requests.get(url15)
    print(response15.content)  """

def stockSplitSpecific():
    url16 = f"https://api.polygon.io/v3/reference/splits?ticker={stock_ticker}&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  #get the historical splits for a specific stock
    print("\nGet the historical splits for a specific stock")
    response16 = requests.get(url16)
    print(response16.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockSplitSpecific.json', 'w') as file:
        json.dump(json.loads(response16.content), file, indent=4)

stockSplitSpecific()

"""        
url16 = f"https://api.polygon.io/v3/reference/splits?ticker={stock_ticker}&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  #get the historical splits for a specific stock
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockSplitSpecific.json', 'w') as file:
    response16 = requests.get(url16)
    print(response16.content)  """

def dividendList():
    url17 = f"https://api.polygon.io/v3/reference/dividends?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  #get a list of historical dividends, including the ticker symbol, the execution date, and the amount of the dividend
    print("\nGet a list of historical dividends, including the ticker symbol, the execution date, and the amount of the dividend")
    response17 = requests.get(url17)
    print(response17.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/DividendList.json', 'w') as file:
        json.dump(json.loads(response17.content), file, indent=4)

dividendList()
#time.sleep(20)  # sleep for 62 seconds before continuing

"""
url17 = f"https://api.polygon.io/v3/reference/dividends?apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  #get a list of historical dividends, including the ticker symbol, the execution date, and the amount of the dividend
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/DividendList.json', 'w') as file:
    response17 = requests.get(url17)
    print(response17.content)
"""

def stockDividendSpecific():
    url18 = f"https://api.polygon.io/v3/reference/dividends?ticker={stock_ticker}&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the historical dividends for a specific stock")
    response18 = requests.get(url18)
    print(response18.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockDividendSpecific.json', 'w') as file:
        json.dump(json.loads(response18.content), file, indent=4)

stockDividendSpecific()

"""
url18 = f"https://api.polygon.io/v3/reference/dividends?ticker={stock_ticker}&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  #get the historical dividends for a specific stock
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockDividendSpecific.json', 'w') as file:
    response18 = requests.get(url18)
    print(response18.content)
"""

def stockConditions():
    url19 = f"https://api.polygon.io/v3/reference/conditions?asset_class=stocks&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet the stock conditions")
    response19 = requests.get(url19)
    print(response19.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockConditions.json', 'w') as file:
        json.dump(json.loads(response19.content), file, indent=4)

stockConditions()

"""
url19 = f"https://api.polygon.io/v3/reference/conditions?asset_class=stocks&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockConditions.json', 'w') as file:
    response19 = requests.get(url19)
    print(response19.content)  """
        
def stockExchanges():
    url20 = f"https://api.polygon.io/v3/reference/exchanges?asset_class=stocks&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"
    print("\nGet a list of all exchanges")
    response20 = requests.get(url20)
    print(response20.content)
    with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockExchanges.json', 'w') as file:
        json.dump(json.loads(response20.content), file, indent=4)

stockExchanges()
"""
url20 = f"https://api.polygon.io/v3/reference/exchanges?asset_class=stocks&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8"  #list of all exchanges
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockExchanges.json', 'w') as file:
    response20 = requests.get(url20)
"""





    #the file saves the data twice
'''
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/data/aggregate-bars.json', 'w') as file:
    file.write(response.content.decode('utf-8'))
'''