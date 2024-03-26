#import api_calls
#import step2
from api_calls import stock_ticker
import openai
import time
import os
import json

openai.api_key = "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" #make sure to remoev this later

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
# import the json files relevant to the api call to access their content
aggregate_bars_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/aggregate-bars.json'

grouped_daily_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/grouped-daily.json'

openClose_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/open-close.json'

previousClose_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/previous-close.json'

simpleMovingAverage_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/sma.json'

exponentialMovingAverage_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/ema.json'

movingAverageConvergenceDivergence_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/macd.json'

relativeStrengthIndex_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/rsi.json'

tickerSymbols_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/tickers.json'

tickerDetails_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/ticker-details.json'

allNews_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/Allnews.json'

specificStockNews_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/SpecificStockNews.json'

marketHolidays_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/MarketHolidays.json'

marketStatus_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/MarketStatus.json'

stockSplitList_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/SplitList.json'

stockSplitSpecific_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockSplitSpecific.json'

dividendList_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/DividendList.json'

stockDividendSpecific_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockDividendSpecific.json'

stockConditions_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockConditions.json'

stockExchanges_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/StockExchanges.json'

#read the json files
aggregate_bars = read_json_file(aggregate_bars_path)
grouped_daily = read_json_file(grouped_daily_path)
openClose = read_json_file(openClose_path)
previousClose = read_json_file(previousClose_path)
simpleMovingAverage = read_json_file(simpleMovingAverage_path)
exponentialMovingAverage = read_json_file(exponentialMovingAverage_path)
movingAverageConvergenceDivergence = read_json_file(movingAverageConvergenceDivergence_path)
relativeStrengthIndex = read_json_file(relativeStrengthIndex_path)
tickerSymbols = read_json_file(tickerSymbols_path)
tickerDetails = read_json_file(tickerDetails_path)
allNews = read_json_file(allNews_path)
specificStockNews = read_json_file(specificStockNews_path)
marketHolidays = read_json_file(marketHolidays_path)
marketStatus = read_json_file(marketStatus_path)
stockSplitList = read_json_file(stockSplitList_path)
stockSplitSpecific = read_json_file(stockSplitSpecific_path)
dividendList = read_json_file(dividendList_path)
stockDividendSpecific = read_json_file(stockDividendSpecific_path)
stockConditions = read_json_file(stockConditions_path)
stockExchanges = read_json_file(stockExchanges_path)

#convert them to strings
aggregate_bars_str = json.dumps(aggregate_bars, indent=4)
grouped_daily_str = json.dumps(grouped_daily, indent=4)
openClose_str = json.dumps(openClose, indent=4)
previousClose_str = json.dumps(previousClose, indent=4)
simpleMovingAverage_str = json.dumps(simpleMovingAverage, indent=4)
exponentialMovingAverage_str = json.dumps(exponentialMovingAverage, indent=4)
movingAverageConvergenceDivergence_str = json.dumps(movingAverageConvergenceDivergence, indent=4)
relativeStrengthIndex_str = json.dumps(relativeStrengthIndex, indent=4)
tickerSymbols_str = json.dumps(tickerSymbols, indent=4)
tickerDetails_str = json.dumps(tickerDetails, indent=4)
allNews_str = json.dumps(allNews, indent=4)
specificStockNews_str = json.dumps(specificStockNews, indent=4)
marketHolidays_str = json.dumps(marketHolidays, indent=4)
marketStatus_str = json.dumps(marketStatus, indent=4)
stockSplitList_str = json.dumps(stockSplitList, indent=4)
stockSplitSpecific_str = json.dumps(stockSplitSpecific, indent=4)
dividendList_str = json.dumps(dividendList, indent=4)
stockDividendSpecific_str = json.dumps(stockDividendSpecific, indent=4)
stockConditions_str = json.dumps(stockConditions, indent=4)
stockExchanges_str = json.dumps(stockExchanges, indent=4)


prompt = (
    f"\n Instruction: Based on the previous mentioned comment of me wanting to invest in the company with the following stock_ticker: {stock_ticker}. "
    f"Additionally take into consideration the following list of financial data that I got from making series of api calls I found regarding the current status of the stock: "
    f"Based on the information provided, I would like to know the best course of action to take in order to maximize my investment, let me know what you think in regards to my decision to invest in the stock {stock_ticker}, take into consideration the following financial data that I have provided below: (Note: please provide a detauled explanation, at least several paragraphs long, to ensure that I have a clear understanding of the best course of action to take in order to maximize my investment.)"
    f"""
    Aggregate Bars: {aggregate_bars_str}
    Grouped Daily: {grouped_daily_str}
    Open Close: {openClose_str}
    Previous Close: {previousClose_str}
    Simple Moving Average: {simpleMovingAverage_str}
    Exponential Moving Average: {exponentialMovingAverage_str}
    Moving Average Convergence Divergence: {movingAverageConvergenceDivergence_str}
    Relative Strength Index: {relativeStrengthIndex_str}
    Ticker Symbols: {tickerSymbols_str}
    Ticker Details: {tickerDetails_str}
    All News: {allNews_str}
    Specific Stock News: {specificStockNews_str}
    Market Holidays: {marketHolidays_str}
    Market Status: {marketStatus_str}
    Stock Split List: {stockSplitList_str}
    Stock Split Specific: {stockSplitSpecific_str}
    Dividend List: {dividendList_str}
    Stock Dividend Specific: {stockDividendSpecific_str}
    Stock Conditions: {stockConditions_str}
    Stock Exchanges: {stockExchanges_str}
"""
    f"additionally based on the data provided, if you believe I would be better off investing in other companies, provide me list of 5-10 additional companies I should consider as means of diversifying my portfolio. "
    f"Lastly, provide me with visualizations based on the data in regards to projected growth, my likelihood of profit/loss, based on the stock list provided what would and wouldn't be considered high risk vs stability.\n"
)