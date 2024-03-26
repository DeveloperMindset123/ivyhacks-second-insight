import sys
# adding this ensures we can import files from other directories as well
sys.path.append('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/api')  
import api_calls

api_calls.stockSplitSpecific()  # test 16
api_calls.dividendList()   # test 17
api_calls.stockDividendSpecific()  # test 18
api_calls.stockConditions()  # test 19
api_calls.stockExchanges()  # test 20