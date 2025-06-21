# import requests

# def get_crypto_price(coin_id):
#     url = f"https://api.coingecko.com/api/v3/simple/price"
#     params = {
#         'ids': coin_id,
#         'vs_currencies': 'usd'
#     }

#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#         if coin_id in data:
#             price = data[coin_id]['usd']
#             print(f"💲 Current price of {coin_id.capitalize()} is: ${price}")
#         else:
#             print("❌ Coin not found. Please check the coin ID.")
#     except Exception as e:
#         print(f"⚠️ Error fetching price: {e}")

# if __name__ == "__main__":
#     coin = input("🔎 Enter cryptocurrency name (e.g., bitcoin, ethereum, dogecoin): ").lower()
#     get_crypto_price(coin)
