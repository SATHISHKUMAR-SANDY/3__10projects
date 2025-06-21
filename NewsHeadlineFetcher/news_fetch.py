# import requests

# API_KEY = '5a69493b653b4e0a894042a1c50aa757'
# URL = 'https://newsapi.org/v2/top-headlines'

# params = {
#     'country': 'us',
#     'apiKey': API_KEY
# }

# response = requests.get(URL, params=params)
# data = response.json()

# print(data)  # Debugging line

# if data['status'] == 'ok' and data['articles']:
#     print("\nTop News Headlines:\n")
#     for i, article in enumerate(data['articles'][:10], 1):
#         print(f"{i}. {article['title']}")
# else:
#     print("\n⚠️ No headlines found or request failed:")
#     print(data.get('message', 'Unknown error'))
