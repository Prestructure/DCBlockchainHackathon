#!/usr/bin/python

import json
import subprocess
import sys
import time

import binascii
import logging
logging.basicConfig(level=logging.INFO)

processed = set()

def init():
    output = subprocess.check_output(['zcash-cli', 'z_listaddresses'])
    zs = json.loads(output)
    return zs[0]

def getTransactions(Z):
    output = subprocess.check_output(['zcash-cli', 'z_listreceivedbyaddress', Z, '0'])
    return json.loads(output)

def process(tx):
    txid = tx['txid']
    memo = tx['memo']
    if txid in processed:
        return None
    processed.add(txid)
    try:
        logging.info('processing %s', txid)
        end = len(memo)
        while (end > 1) and (memo[end - 2: end] == '00'):
            end -= 2
        memo = binascii.unhexlify(memo[0:end])
        print memo
        print 'memo: ' + memo
        d = json.loads(memo)
        return d
    except Exception as e:
        logging.exception(e)
        return None

while True:
    Z = init()
    ts = getTransactions(Z)
    for t in ts:
        memo = process(t)
        if memo:
            print 'JACKPOT: ' + json.dumps(memo)
            print
    time.sleep(1)
