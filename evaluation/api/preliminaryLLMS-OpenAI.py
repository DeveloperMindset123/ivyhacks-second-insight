from numpy import matrix
import openai
import json
import os
# Set up OpenAI API credentials
openai.api_key = "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"
# Generate text using OpenAI GPT-3 model
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a stock portfolio manager who provides insight based on user's stock portfolio image from various platform"},
        {"role": "user", "content": "I want to invest in an tesla, what does the outcome look like in 6 months, 1 year, and 5 year, provide me a detailed description."}
    ],
    max_tokens=200,
    n=1,
    temperature=0.7
)



generated_text = response.choices[0].message 
print(generated_text)

# Calculate appropriate matrix for model's response
def measure_relevance(text):
    # Logic to measure the relevance of the response
    # You can use NLP techniques like keyword matching, semantic similarity, or machine learning models
    
    relevance_score = 0.8  # Placeholder value, replace with actual relevance score
    
    return relevance_score


def measure_quality(text):
    # Logic to measure the quality of the response
    # You can use NLP techniques like grammar checking, readability analysis, or machine learning models
    
    quality_score = 0.9  # Placeholder value, replace with actual quality score
    
    return quality_score


def measure_accuracy(text):
    # Logic to measure the accuracy of the response
    # You can use NLP techniques like fact-checking, source verification, or machine learning models
    
    accuracy_score = 0.85  # Placeholder value, replace with actual accuracy score
    
    return accuracy_score


def measure_sentiment(text):
    # Logic to measure the sentiment of the response
    # You can use NLP techniques like sentiment analysis, emotion detection, or machine learning models
    
    sentiment_score = 0.7  # Placeholder value, replace with actual sentiment score
    
    return sentiment_score


def calculate_matrix(text):
    # Measure the relevance of the response
    relevance = measure_relevance(text)
    
    # Measure the quality of the response
    quality = measure_quality(text)
    
    # Measure the accuracy of the response
    accuracy = measure_accuracy(text)
    
    # Measure the sentiment of the response
    sentiment = measure_sentiment(text)
    
    # Create a matrix with the calculated values
    matrix = {
        'relevance': relevance,
        'quality': quality,
        'accuracy': accuracy,
        'sentiment': sentiment
    }
    
    return matrix
# Save the response and matrix in a JSON file
result = {'response': generated_text, 'matrix': matrix}
with open('/result/output.json', 'w') as json_file:
    json.dump(result, json_file)

# Save the response in a text file
with open('/result/output.txt', 'w') as text_file:
    text_file.write(generated_text)

    '''
# Set up OpenAI API credentials
openai.api_key = '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'

# Generate text using OpenAI GPT-3 model
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
   # engine="text-davinci-003",
    messages=[
        {"role": "system", "content": "You are a stock portfolio manager who provides insight based on user's stock portfolio image from various platform"},
        {"role": "user", "content": "I want to invest in an tesla, what does the outcome look like in 6 months, 1 year, and 5 year, provide me a detailed description."}
    ],
    max_tokens=200,
    n=1,
    temperature=0.7
)

# Get the generated text
generated_text = response.choices[0].message 
print(generated_text)
# Save the response in a JSON file


with open('/result/output.json', 'w') as json_file:
        json.dump({'response': generated_text}, json_file)

# Save the response in a text file
with open('/result/output.txt', 'w') as text_file:
        text_file.write(generated_text) 
        '''