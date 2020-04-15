
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

# read data values for Bisley Q3 from LCZO sensor database
# display tamperature values in a graph

# hs = hydroshare.hydroshare('miguelcleon')
# content = hs.getResourceFromHydroShare('e049f19dc8ba46c98754711da2ab6030')

# LCZOSensorDB = hs.content['LCZO-ODM2-MariaTimeSeries.sqlite']
# engine = create_engine('sqlite:///C:\\Users\\12672\\Box\\data\\NEON\\lczodata\\LCZO-ODM2-MariaTimeSeries3.sqlite')
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
                                                 endtime= '2017-10-30')
# 17182
datetimes = airtempQ3['ValueDateTime']
airtemp = airtempQ3['DataValue']

plt.plot(datetimes, airtemp)
plt.gcf().autofmt_xdate()
plt.show()

