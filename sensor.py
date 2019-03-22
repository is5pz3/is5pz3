#!/usr/bin/python3

import psutil as psu
import time

while(True):
    cpu = psu.cpu_percent()
    ram = psu.virtual_memory()
    print("CPU {}%".format(cpu))
    print("RAM total: {}GB \t used: {}GB {}%".format(round(ram.total / pow(2,30), 2), round(ram.used / pow(2,30), 2), ram.percent))
    time.sleep(1)