import openai
from step3 import prompt


extended_prompt="Note that the information provided is the json response based on the previous api calls that were made, utilize this as part of upto date financial information to make the decision on the best course of action to take in order to maximize the investment, provide a list of 5-10 additional companies to consider as means of diversifying the portfolio, and provide visualizations based on the data in regards to projected growth, likelihood of profit/loss, and what would and wouldn't be considered high risk vs stability."

response = openai.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "You are a stock portfolio manager who provides insight based on user's goal of investing based on their prompt from various platforms"},
        {"role": "user", "content": prompt+extended_prompt},
                #{"role": "system", "content": "Here is some historical data to improve accuracy: " + str(get_historical_data())[:1000]}  #limit the tokens
    ],
    max_tokens=4050,
    n=1,
    temperature=0.6
)

generated_text = response.choices[0].message.content    
print("generated text")
print(generated_text)  # the model seems to correctly output the appropriate json format --> manually save it into the 

extracted_info_file_path="/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/extracted_info2.txt"  # ensure that the file path is correct
with open(extracted_info_file_path, 'w') as file:
    file.write(generated_text)
print(f"Output saved to {extracted_info_file_path}")