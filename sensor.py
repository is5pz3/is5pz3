#!/usr/bin/python3

import psutil
import pause
import requests
import platform
import argparse
import socket
import json
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--name', '-n', help="sensor name",
                    type=str, required=False)
parser.add_argument('--address', '-a', help="host address",
                    type=str, required=True)
parser.add_argument('--interval', '-i',
                    help="inteval in seconds", type=float, default=1.0)
args = parser.parse_args()

headers = {'Content-type': 'application/json'}

init_data = {
    "sensor_id": args.name,
    "host_name": "Desktop",
    "platform": platform.system(),
    "metric": "RamUsage",
    "unit": "%"
}
r = requests.post(args.address + '/hosts', data=json.dumps(init_data), headers=headers)
print(r.json())
print(r)
if(r.status_code >= 200 and r.status_code < 400):
    while(True):
        timestamp = datetime.timestamp(datetime.now())
        msrmnt = {
            "timestamp": int(timestamp),
            "value": psutil.cpu_percent()
        }
        try:
            rv = requests.post(args.address + '/hosts/' + args.name, data=json.dumps(msrmnt), headers=headers)
            print(rv.json())
        except:
            print("nobody cares")
        pause.until(datetime.fromtimestamp(timestamp + args.interval))
else:
    print("NO CONNECTION")
