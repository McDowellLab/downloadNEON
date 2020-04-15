
import sys
import os
import pprint
import numpy
import getpass
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from sqlalchemy import create_engine
from sqlalchemy import orm
from utilities import hydroshare
from odm2api.ODM2.services.readService import *
from odm2api.ODM2.services.createService import *
from odm2api.ODMconnection import dbconnection
import odm2api.ODM2.services.readService as odm2
from odm2api.ODM2.services.readService import *
from odm2api.ODM2.services.createService import *
from odm2api.ODM2.models import *
import dateutil.parser
import csv
from datetime import datetime

# display LCZO and NEON air temp data together

# path for desktop
# C:\\Users\\12672\\Box\\data\\NEON\\lczodata\\LCZO-ODM2-MariaTimeSeries3.sqlite

session_factory = dbconnection.createConnection('sqlite', 'C:\\Users\\leonmi\\Desktop\\BoxUNH\\Box Sync\\data\\NEON\\lczodata\\LCZO-ODM2-MariaTimeSeries3.sqlite')
dbsession = session_factory.getSession()

read = ReadODM2(session_factory)
write = CreateODM2(session_factory)

samplingfeatures = read.getSamplingFeatures()
samplingfeatureids = []
samplingfeaturenames = {}

for sf in samplingfeatures:
    print(sf)
resultidlist = 17268
airtempQ3 = read.getResultValues(resultidlist, starttime='2017-01-01',
                                                 endtime= '2017-12-30')
print(airtempQ3)
# 17182
datetimesLCZO = airtempQ3['ValueDateTime']
datetimesLCZO2 = []
airtempLCZO = airtempQ3['DataValue']

for dt in datetimesLCZO:
    # print(dt)
    datetimesLCZO2.append(datetime.strptime(str(dt), '%Y-%m-%d %H:%M:%S'))
#NEON air temp


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

                        if datet > dateutil.parser.parse('2018-01-01T00:00:00Z'):
                            break
                    except ValueError:
                        print(row[1])
                        print(row[2])
fig, ax = plt.subplots()

ax.scatter(datetimesLCZO2, airtempLCZO, color='darkolivegreen', label='Mameyes tributary - Bisley Q3',alpha=0.9,s=0.8)
ax.scatter(datetimes, airtemp, color='darkkhaki',  label='Guanica Forest',alpha=0.6,s=0.8)

fig.autofmt_xdate()
ax.set_xlim([datetime(2017, 1, 1), datetime(2017, 11, 1)])
# ax.xlabel('Air temperature at Guanica Foroest and Quebrada Sonadora near El Verde')
# h1, l1 = ax1.get_legend_handles_labels()
# h2, l2 = ax2.get_legend_handles_labels()
# print(ax2)
plt.legend()
# plt.legend(h1+h2, l1+l2, loc=2)
ax.set_ylabel('Air temperature degrees celsius')
ax.set_title('Air temperature at Guanica Forest and Mameyes tributary - Bisley Q3')

# plt.plot(datetimes,airtemp)
# plt.gcf().autofmt_xdate()
# plt.show()
# plt.plot(datetimesLCZO, airtempLCZO)
# plt.gcf().autofmt_xdate()
plt.show()