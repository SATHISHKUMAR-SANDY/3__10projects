# import pandas as pd
# import smtplib
# import ssl
# from email.message import EmailMessage

# # --- Config ---
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 465  # For SSL
# SENDER_EMAIL = "youremail@gmail.com"
# SENDER_PASSWORD = "your_app_password"  # Use App Password for Gmail

# # --- Email content ---
# SUBJECT = "Hello from Python!"
# BODY_TEMPLATE = """
# Hi {name},

# This is a test email sent using Python SMTP with CSV contacts.

# Regards,
# Your Python Script
# """

# # --- Load contacts from CSV ---
# def load_contacts(filename):
#     return pd.read_csv(filename)

# # --- Send Email ---
# def send_email(to_email, to_name):
#     msg = EmailMessage()
#     msg["Subject"] = SUBJECT
#     msg["From"] = SENDER_EMAIL
#     msg["To"] = to_email
#     body = BODY_TEMPLATE.format(name=to_name)
#     msg.set_content(body)

#     try:
#         with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=ssl.create_default_context()) as server:
#             server.login(SENDER_EMAIL, SENDER_PASSWORD)
#             server.send_message(msg)
#             print(f"✅ Email sent to {to_name} <{to_email}>")
#     except Exception as e:
#         print(f"❌ Failed to send to {to_email}: {e}")

# # --- Main Function ---
# def main():
#     contacts = load_contacts("contacts.csv")
#     for _, row in contacts.iterrows():
#         send_email(row["email"], row["name"])

# if __name__ == "__main__":
#     main()
