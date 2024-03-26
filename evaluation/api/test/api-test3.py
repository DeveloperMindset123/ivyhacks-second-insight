import sys
# adding this ensures we can import files from other directories as well
sys.path.append('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/api')  
import api_calls


api_calls.allNews()  # test 11
api_calls.specificStockNews()  # test 12
api_calls.marketHolidays()  # test 13
api_calls.marketStatus()  # test 14
api_calls.stockSplitList()  # test 15