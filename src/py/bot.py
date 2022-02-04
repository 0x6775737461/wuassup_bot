from twilio.rest import Client 

from dotenv import load_dotenv
import os

import logging

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN") 
twilio_num = os.getenv("TWILIO_NUM")
my_num = os.getenv("MY_NUM")

client = Client(account_sid, auth_token) 

logging.basicConfig()
client.http_client.logger.setLevel(logging.INFO)

# getting the 'last' 1 msg
msgs = client.messages.list(limit=1)

for msg in msgs:
    print(f"{msg.from_}: {msg.body}\n")

    if msg.body == '/ahoy':
        message = client.messages.create(
            from_ = 'whatsapp:' + twilio_num,
            body = 'AHOY!!',
            to = msg.from_
        )
