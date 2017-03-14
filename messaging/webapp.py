
from flask import Flask
from flask import request

import json
import logging
import time
import thread

app = Flask(__name__)


def poll ():
    while True:
        logging.info('polling')
        time.sleep(5)

context = {

}

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/messages')
def get_messages():
    seq = request.args.get('seq')
    return seq

@app.route('/messages/send/<z>', methods=['POST'])
def add_message(z):
    message = request.get_json()
    body = json.dumps(message)
    print z
    logging.info('sending to %s: %s', z, message)
    # todo: actually send the message
    return 'message sent'

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    thread.start_new_thread(poll, ())
    app.run()
    logging.info('app is running')
