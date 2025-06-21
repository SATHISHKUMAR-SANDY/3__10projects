# from twilio.rest import Client
# from dotenv import load_dotenv
# import os

# # 🔄 Load environment variables from .env file
# load_dotenv()

# # ✅ Get credentials and phone numbers from environment
# account_sid = os.getenv("TWILIO_SID")
# auth_token = os.getenv("TWILIO_AUTH_TOKEN")
# twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
# to_number = os.getenv("TO_PHONE_NUMBER")

# # 🔐 Initialize Twilio client
# client = Client(account_sid, auth_token)

# # 📤 Send SMS
# message = client.messages.create(
#     body="🚀 Hello! This is a test SMS from your Python app.",
#     from_=twilio_number,
#     to=to_number
# )

# # ✅ Confirmation
# print(f"✅ Message sent. SID: {message.sid}")
