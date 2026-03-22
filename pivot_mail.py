import yfinance as yf
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# -------- CONFIG --------
STOCK = "TATASTEEL.NS"

EMAIL_SENDER = "deepakraj6380@gmail.com"
EMAIL_PASSWORD = "osfifrhdzxfcyzbt"
EMAIL_RECEIVER = "deepakrajdro@gmail.com"

# -------- FETCH DATA --------
data = yf.download(STOCK, period="2d", interval="1d")

if len(data) < 2:
    raise Exception("Not enough data")

prev = data.iloc[-2]

high = prev['High']
low = prev['Low']
close = prev['Close']

# -------- CALCULATIONS --------
pp = (high + low + close) / 3
r1 = (2 * pp) - low
s1 = (2 * pp) - high

# -------- EMAIL CONTENT --------
message = f"""
Stock: Tata Steel

Date: {datetime.now().strftime('%Y-%m-%d')}

Previous Day:
High: {high:.2f}
Low: {low:.2f}
Close: {close:.2f}

Pivot Levels:
PP: {pp:.2f}
R1: {r1:.2f}
S1: {s1:.2f}
"""

msg = MIMEText(message)
msg['Subject'] = "Daily Pivot - Tata Steel"
msg['From'] = EMAIL_SENDER
msg['To'] = EMAIL_RECEIVER

# -------- SEND EMAIL --------
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.send_message(msg)

print("Email sent successfully")
