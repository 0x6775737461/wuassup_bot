'''
simple wpp bot to reply msgs
'''

import os
#import logging
import time

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
twilio_num = os.getenv("TWILIO_NUM")
my_num = os.getenv("MY_NUM")

client = Client(account_sid, auth_token)

#logging.basicConfig()
#client.http_client.logger.setLevel(logging.INFO)

def get_msg_struct():
    '''
    get the 'last' msg  in the last 1sec
    and return a msg struct
    '''

    # getting the 'last' 1 msg
    msgs = client.messages.list(limit=1)

    time.sleep(1)

    return msgs

def send_msg(msg, sender):
    '''
    just send a simple msg
    '''

    client.messages.create(
        from_ = 'whatsapp:' + twilio_num,
        body = msg,
        to = sender
    )

def ahoy_reply(msg, sender):
    '''
    send 'AHOY' when receive '/ahoy'
    '''

    if msg == '/ahoy':
        send_msg('AHOY!!', sender)

def main():
    while True:
        msgs = get_msg_struct()

        for msg in msgs:
            ahoy_reply(msg.body, msg.from_)

if __name__ == '__main__':
    main()
