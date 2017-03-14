#!/usr/bin/python

import argparse
import binascii
import json
import logging
import subprocess
import sys
import time

def main():
     logging.basicConfig(level=logging.INFO)
     parser = argparse.ArgumentParser()
     parser.add_argument('--from-address')
     parser.add_argument('--to-address')
     args = parser.parse_args()
     to_address = args.to_address
     from_address = args.from_address
     for line in sys.stdin:
          rawMemo = line.strip()
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
          time.sleep(5)

main()
