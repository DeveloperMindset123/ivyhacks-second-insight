import sys
# adding this ensures we can import files from other directories as well
sys.path.append('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/api')  
import api_calls

api_calls.aggregateBars()  # test 1
api_calls.dailyOpenHighLowCloseVolume()  # test 2
api_calls.openClose()  # test 3
api_calls.previousClose() # test 4
api_calls.simpleMovingAverage()  # test 5
