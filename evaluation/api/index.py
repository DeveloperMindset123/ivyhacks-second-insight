import csv
import datetime
import json
import openai
import pandas as pd

from test3 import get_historical_data

stock_info_file = pd.read_csv('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/data/stock_info.csv')

stock_info = "/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/stock_info.csv"
# Read the stock_info.csv file
with open(stock_info, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    stock_info = {row[1]: row[0] for row in csv_reader}
print("CSV transformed to dataframe:")
print(stock_info_file)


company_data = stock_info_file.to_dict()
print("Dataframe converted to dictionary:")
print(company_data)


# Function to extract the NLP prompt from the given file
def extract_nlp_prompt(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        prompt_start = content.find('"{')
        prompt_end = content.find('}"') + 2
        nlp_prompt = content[prompt_start:prompt_end]
    return nlp_prompt

# Define the company data with stock tickers
'''
company_data = {
        'apple': 'AAPL',
        'google': 'GOOGL',
        'amazon': 'AMZN',
        # Add more companies and their stock tickers here
} '''


    # Function to determine the company and check the corresponding stock ticker
def determine_stock_ticker(nlp_prompt, company_data):
        # Assuming the NLP prompt contains the company name
        company_name_start = nlp_prompt.find('invest in') + len('invest in')
        company_name_end = nlp_prompt.find(',', company_name_start)
        company_name = nlp_prompt[company_name_start:company_name_end].strip()
        # Check if the company name exists in the company data
        if company_name.lower() in company_data:
            stock_ticker = company_data[company_name.lower()]
            return stock_ticker
        else:
            return None
        
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Define the NLP prompt
nlp_prompt = f"I want to invest $4000 in Apple for 1 year from now, today's date is ${current_date}.\n"

    # Extract the NLP prompt from the file
    #nlp_prompt = extract_nlp_prompt('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/step1.py')

    # Determine the stock ticker
stock_ticker = determine_stock_ticker(nlp_prompt, company_data)
print(stock_ticker)

    # Define the starting and ending investment dates --> hardcoded
investment_amount = 4000  # Define the investment amount
start_date = datetime.datetime.now().strftime("%Y-%m-%d")
end_date = (datetime.datetime.now() + datetime.timedelta(days=365)).strftime("%Y-%m-%d")

# Create a dictionary to store the extracted information
extracted_info = {
    'stock_ticker': stock_ticker,
    'start_date': start_date,
    'end_date': end_date,
    'investment_amount': investment_amount
}


# Save the extracted information to a separate JSON file
extracted_info_file = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/extracted_info.txt'
#end of hardcoded value, start of dynamic logic

    #json.dump(extracted_info, file)

if stock_ticker is None:
        # Use OpenAI API to determine the stock ticker
        # Make the API call and get the response
    extended_prompt="\n Instruction: Based on the above prompt provided, determine the stock_ticker corresponding to the company mentioned in the prompt, alongside the current timestamp for the starting investment date and the timestamp for the ending investment date, generate an output in json format containing the stock_ticker, start_date, end_date based on when the user wants to stop investing and the investment amount, watch out for the keyword 'from now', since that will indicate the present to how long the user wants to invest, figure out the math as it would be from current timestamp to the time the user wants to stop investing, which means the start and end date won't be the same as one another, it could be (at minimum 6 months or longer, this is dependent on the infomration provided by the user in the prompt), genereally the amount can be found attached to $ icon in the prompt"
    response = openai.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a stock portfolio manager who provides insight based on user's goal of investing based on their prompt from various platforms"},
            {"role": "user", "content": nlp_prompt+extended_prompt},
                #{"role": "system", "content": "Here is some historical data to improve accuracy: " + str(get_historical_data())[:1000]}  #limit the tokens
        ],
        max_tokens=200,
        n=1,
        temperature=0.7
    )

    generated_text = response.choices[0].message.content    
    print("generated text")
    print(generated_text)  # the model seems to correctly output the appropriate json format --> manually save it into the 

    extracted_info_file_path="/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/Data/extracted_info.txt"  #ensure the file path is correct here
    with open(extracted_info_file_path, 'w') as file:
        file.write(generated_text)

    print(f"Output saved to {extracted_info_file_path}")



        
'''
        try:
            response_data = json.loads(generated_text.strip('json'))
            print(response_data)
        except json.JSONDecodeError as e:
            print("Failed to decode JSON:", e)

            
        response_data = json.loads(generated_text.strip())
        stock_ticker = response_data['stock_ticker']
        end_date = response_data['end_date']
        investment_amount = response_data['investment_amount']

        # Create a dictionary to store the extracted information
        extracted_info = {
            'stock_ticker': stock_ticker,
            'start_date': start_date,
            'end_date': end_date,
            'investment_amount': investment_amount
        }

        # Save the extracted information to a separate JSON file
        extracted_info_file = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/LLMSResponse/extracted_info.json'
        with open(extracted_info_file, 'w') as file:
            json.dump(extracted_info, file)
            '''