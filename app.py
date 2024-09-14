import os
import requests

# Fetch CryptoPanic API key from environment variables
api_key = os.getenv('CRYPTOPANIC_API_KEY')

# Define the base URL and parameters for the API request
url = "https://cryptopanic.com/api/v1/posts/"
params = {
    'auth_token': api_key,
    'currencies': 'BTC,ETH',  # Fetch news for Bitcoin and Ethereum
    'public': 'true'  # Only public posts
}

# Make the request to the API
response = requests.get(url, params=params)

# Check the status of the request
if response.status_code == 200:
    news_data = response.json()
    articles = news_data.get('results', [])
    for i, article in enumerate(articles[:5]):  # Fetch the first 5 articles for now
        print(f"Article {i + 1}:")
        print("Title:", article['title'])
        print("URL:", article['url'])
        print("Published:", article['published_at'])
        print("\n")
else:
    print(f"Failed to fetch news. Status code: {response.status_code}")
