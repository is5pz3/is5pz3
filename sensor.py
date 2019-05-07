#!/usr/bin/python3

import psutil as psu
import time
import requests
import platform
import argparse
import socket
import json

parser = argparse.ArgumentParser()
parser.add_argument('--address', '-a', help="host address",
                    type=str, required=True)
parser.add_argument('--interval', '-i',
                    help="inteval in seconds", type=float, default=1.0)
args = parser.parse_args()

while(True):
    cpu = psu.cpu_percent()
    ram = psu.virtual_memory()
    print(socket.gethostname())
    print(args.address)
    print(platform.system() + " "+platform.release())
    print("CPU {}%".format(cpu))
    print("RAM total: {}GB \t used: {}GB {}%".format(
        round(ram.total / pow(2, 30), 2), round(ram.used / pow(2, 30), 2), ram.percent))
    msrmnt = {}
    try:
        requests.post(args.address, data=json.dumps(msrmnt))
    except:
        print("nobody cares")
    time.sleep(args.interval)
