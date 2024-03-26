import openai
import json
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
import os
from urllib.request import urlopen
from urllib.request import urlopen
import certifi
import json
import ssl

nltk.download('punkt')
# Set up OpenAI API credentials
openai.api_key = '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' #os.environ.get('OPENAI_API_KEY')
# Set up OpenAI API credentials
#openai.api_key = 'your_api_key_here'  # Replace with your actual API key

# Function to make API call and get historical data
def get_historical_data():
    try:
        context = ssl.create_default_context(cafile=certifi.where())
        url = "https://financialmodelingprep.com/api/v3/historical-price-full/TSLA?from=2015-01-01&to=2024-03-21&apikey=5jcrkWvpQhgrkubqVPDAfjHs1wrbFin7"  #make sure that it is fetching the api call to TSLA
        response = urlopen(url, context=context)
        data = response.read().decode("utf-8")
        return json.loads(data)
    except Exception as e:
        print("Error fetching historical data:", e)
        return {}

# Generate text using OpenAI GPT-3 model
response = openai.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "You are a stock portfolio manager who provides insight based on user's stock portfolio image from various platforms"},
        {"role": "user", "content": "I want to invest in Tesla, what does the outcome look like in 6 months, 1 year, and 5 years, provide me a detailed description."},
        {"role": "system", "content": "Here is some historical data to improve accuracy: " + str(get_historical_data())[:1000]}  #limit the tokens
    ],
    max_tokens=200,
    n=1,
    temperature=0.7
)

generated_text = response.choices[0].message.content

def measure_relevance(text, query):
    query_keywords = set(word_tokenize(query.lower()))
    response_keywords = set(word_tokenize(text.lower()))
    common_keywords = query_keywords.intersection(response_keywords)
    relevance_score = len(common_keywords) / len(query_keywords)
    return relevance_score

def measure_quality(text):
    sentences = text.split('.')
    average_sentence_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences)
    quality_score = average_sentence_length / 20
    return min(1.0, max(0.0, quality_score))

def measure_accuracy(text):
    # This is a placeholder function. Replace this logic with your accuracy assessment criteria.
    sentiment_score = measure_sentiment(text)
    if sentiment_score > 0.8:
        accuracy_score = 5
    elif sentiment_score > 0.6:
        accuracy_score = 4
    elif sentiment_score > 0.4:
        accuracy_score = 3
    elif sentiment_score > 0.2:
        accuracy_score = 2
    else:
        accuracy_score = 1
    return accuracy_score

def measure_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    sentiment_score = (sentiment + 1) / 2
    return sentiment_score

def calculate_matrix(text, query):
    relevance = measure_relevance(text, query)
    quality = measure_quality(text)
    accuracy = measure_accuracy(text)
    sentiment = measure_sentiment(text)
    matrix = {
        'relevance': relevance,
        'quality': quality,
        'accuracy': accuracy,
        'sentiment': sentiment
    }
    matrix_explanation = """
    The matrix provides a score from 0 to 5 on various aspects of the response's quality. 
    'Relevance' measures how closely the response aligns with the user's query. 
    'Quality' assesses the readability and structure of the response. 
    'Accuracy' estimates the reliability of the prediction based on sentiment analysis, with 5 being the most optimistic or positive outlook. 
    'Sentiment' gives an overall sentiment score of the response, normalized between 0 (negative) and 1 (positive).
    """
    return matrix, matrix_explanation

query = "I want to invest in Tesla, what does the outcome look like in 6 months, 1 year, and 5 years, provide me a detailed description."
matrix, matrix_explanation = calculate_matrix(generated_text, query)

response_to_save = {
    "goal": query,
    "context": {"timestamp": "2024-03-23", "text": "I have 100K cash in saving account"}
}

result = {
    'response': generated_text,
    'matrix': matrix,
    'matrix_explanation': matrix_explanation,
    'user_request': response_to_save
}

# Specify the correct path for your environment
json_file_path = '/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/bitMoreAdvanced-response.json'  #corrected file pathing after migration

with open(json_file_path, 'w') as json_file:
    json.dump(result, json_file, indent=4)

print(f"Results saved to {json_file_path}")