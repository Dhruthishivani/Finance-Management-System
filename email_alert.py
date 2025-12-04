import smtplib
import ssl

def send_email_alert(to_email, message):
    sender = "your_email@gmail.com"          # ✅ your real Gmail
    password = "your_16_digit_app_password" # ✅ NOT your Gmail login password

    subject = "💰 Expense Budget Alert"
    body = f"Subject: {subject}\n\n{message}"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, to_email, body)
