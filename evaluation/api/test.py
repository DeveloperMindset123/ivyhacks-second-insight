import openai
import json
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Set up OpenAI API credentials
openai.api_key = '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'

# Generate text using OpenAI GPT-3 model
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a stock portfolio manager who provides insight based on user's stock portfolio image from various platform"},
        {"role": "user", "content": "I want to invest in Tesla, what does the outcome look like in 6 months, 1 year, and 5 years, provide me a detailed description."}
    ],
    max_tokens=200,
    n=1,
    temperature=0.7
)

generated_text = response.choices[0].message.content

def measure_relevance(text, query):
    # A simplistic relevance measure based on keyword matching
    query_keywords = set(word_tokenize(query.lower()))
    response_keywords = set(word_tokenize(text))
    common_keywords = query_keywords.intersection(response_keywords)
    relevance_score = len(common_keywords) / len(query_keywords)
    return relevance_score

def measure_quality(text):
    # A simplistic quality measure based on average sentence length
    sentences = text.split('.')
    if len(sentences) == 0:
        return 0
    average_sentence_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences)
    quality_score = average_sentence_length / 20  # Assuming 20 words as ideal average sentence length
    return min(1.0, max(0.0, quality_score))  # Clamping the score between 0 and 1

def measure_accuracy(text):
    # Placeholder for accuracy measurement
    # In a real scenario, this could involve comparing with factual data or expert analysis
    accuracy_score = 0.85  # Placeholder value
    return accuracy_score

def measure_sentiment(text):
    # Using TextBlob for a simple sentiment analysis
    sentiment = TextBlob(text).sentiment.polarity
    sentiment_score = (sentiment + 1) / 2  # Normalize to 0 to 1
    return sentiment_score

def calculate_matrix(text, query):
    relevance = measure_relevance(text, query)
    quality = measure_quality(text)
    accuracy = measure_accuracy(text)
    sentiment = measure_sentiment(text)
    return {
        'relevance': relevance,
        'quality': quality,
        'accuracy': accuracy,
        'sentiment': sentiment
    }

# Calculating the matrix for the generated text
query = "I want to invest in Tesla, what does the outcome look like in 6 months, 1 year, and 5 years, provide me a detailed description."
matrix = calculate_matrix(generated_text, query)

# Example response to be saved
response_to_save = {
   "goal": query,
   "context": {"timestamp": "2024-03-23", "text": "I have 100K cash in saving account"}
}

# Including the response and matrix in the result
result = {'response': generated_text, 'matrix': matrix, 'user_request': response_to_save}

# Save the result in a JSON file
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/output.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

# Save the response in a text file
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/output.txt', 'w') as text_file:
    text_file.write(generated_text)
