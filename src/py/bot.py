from twilio.rest import Client 

from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN") 
twilio_num = os.getenv("TWILIO_NUM")
my_num = os.getenv("MY_NUM")

client = Client(account_sid, auth_token) 

message = client.messages.create( 
    from_='whatsapp:' + twilio_num,  
    body='TESTANDO O TWILLIO CARAIO!!',      
    to='whatsapp:' + my_num 
) 

print(message.sid)
