
from flask import Flask
from flask import request

import argparse
import binascii
import json
import logging
import subprocess
import time
import thread


#
# python webapp.py --z <YOUR_Z_ADDRESS>
#
# to get messages, do GET localhost:5000/messages?seq=0
# you will get back json with two fields: messages and seq
##
# to send a message do POST locahost:5000/messages/send/<RECEIVERS_Z_ADDRESS>
# with json request body
#

app = Flask(__name__)

context = {
    'transactions': {}
}

def poll_for_incoming():
    while True:
        logging.info('polling')
        t = int(round(time.time()))
        output = subprocess.check_output(['zcash-cli', 'z_listreceivedbyaddress', context['z'], '0'])
        transactions = json.loads(output)
        for tx in transactions:
            txid = tx['txid']
            memo = tx['memo']
            if txid in context['transactions']:
                pass
            else:
                logging.info('new transaction %s', txid)
                try:
                    end = len(memo)
                    while (end > 1) and (memo[end - 2: end] == '00'):
                        end -= 2
                    memo = binascii.unhexlify(memo[0:end])
                    logging.info('parsed memo: %s', memo)
                    d = json.loads(memo)
                    logging.info('json memo: %s', d)
                    context['transactions'][txid] = (t, d)
                except Exception as e:
                    logging.exception(e)
                    context['transactions'][txid] = (t, None)
        time.sleep(10)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/messages')
def get_messages():
    seq = int(request.args.get('seq'))
    new_seq = 0
    messages = []
    for k,v in context['transactions'].items():
        (t, memo) = v
        if t > new_seq:
            new_seq = t
        if memo is not None and t > seq:
            messages.append(memo)
    return json.dumps({
        'seq': new_seq,
        'messages': messages
    })

@app.route('/messages/send/<to_address>', methods=['POST'])
def send_message(to_address):
    from_address = context['z']
    rawMemo = json.dumps(request.get_json())
    memo = binascii.hexlify(rawMemo)
    transactions = [{
        'address': to_address,
        'memo': memo,
        'amount': 0.01
    }]
    transaction_text = json.dumps(transactions)
    minconf = '0'
    logging.info('sending %s', transaction_text)
    output = subprocess.check_output([
        'zcash-cli',
        'z_sendmany',
        from_address,
        transaction_text,
        minconf
    ])
    logging.info('result: %s',  output)
    return 'message sent'

if __name__ == "__main__":
     parser = argparse.ArgumentParser()
     parser.add_argument('--z')
     args = parser.parse_args()
     if not args.z:
         raise Exception('please pass --z')
     else:
         context['z'] = args.z

     logging.basicConfig(level=logging.INFO)
     thread.start_new_thread(poll_for_incoming, ())
     app.run()
     logging.info('app is running')
