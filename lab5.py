#!/bin/bash

import subprocess
import os
import csv
import time


def get_load():

 try:
   s = subprocess.check_output(["cat","/proc/loadavg"])
   return float(s.split()[0])
 except:
   return 0  


def get_ram():

   try:
        s = subprocess.check_output(["free","-m"])
        lines = s.split("\n")
        used_mem = float(lines[1].split()[2])
        total_mem = float(lines[1].split()[1])
        return (int((used_mem/total_mem)*100))
   except:
        return 0


def get_disk():

    try:
        s = subprocess.check_output(["df","/dev/root"])
        lines = s.split("\n")
        return int(lines[1].split("%")[0].split()[4])
    except:
        return 0


def get_temperature():

 try:
   tempC = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
   return tempC
 except:
   return 0

# .......................................MAIN........................................
#myrecord = dict()
file_name = "stats.txt"
file_out = open(file_name,'w')

try:

 writer = csv.writer(file_out)
 fieldnames = ('date','load','ram','disk','temperature')
 writer = csv.DictWriter(file_out, fieldnames=fieldnames,delimiter = '\t')
 headers = dict((n,n) for n in fieldnames)
 writer.writerow(headers)

 while True:

    print "load:",get_load()
    print "ram:",get_ram()
    print "disk:",get_disk()
    print "Temp:",get_temperature()
    time.sleep(2)
    print "Recording Data Into a FILE:",file_name
    timestamp = time.strftime("%m-%d-%Y-%H:%M:%S")
    writer.writerow({'date':timestamp,'load':get_load(),'ram':get_ram(),'disk':get_disk(),'temperature':get_temperature()})
  
except KeyboardInterrupt:
 file_out.close()
#..........................................END.................................


