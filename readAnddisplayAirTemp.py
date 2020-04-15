import requests
import json
import csv
import urllib.request
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import dateutil.parser

# read NEON air temperature files for Guanica Forest and plot on a graph
airtempfiles = []
import os
rootdir = './airtemp'
airtemp = []
datetimes = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + '/' + file
        if 'basic' in filepath:
            print(filepath)
            with open(filepath,'r')as tempfile:
                reader = csv.reader(tempfile)
                for row in reader:

                    try:
                        airtemp.append(float(row[2]))
                        datet = dateutil.parser.parse(row[1])
                        datetimes.append(datet)
                    except ValueError:
                        print(row[1])
                        print(row[2])
plt.plot(datetimes,airtemp)
plt.gcf().autofmt_xdate()
plt.show()
