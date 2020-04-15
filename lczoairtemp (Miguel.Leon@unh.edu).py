
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
# conda install --no-deps -c conda-forge odm2api
# hs = hydroshare.hydroshare('miguelcleon')
# content = hs.getResourceFromHydroShare('e049f19dc8ba46c98754711da2ab6030')

# LCZOSensorDB = hs.content['LCZO-ODM2-MariaTimeSeries.sqlite']
# engine = create_engine('sqlite:///C:\\Users\\12672\\Box\\data\\NEON\\lczodata\\LCZO-ODM2-MariaTimeSeries3.sqlite')
# loc = 'C:\\Users\\12672\\Box\\data\\NEON\\lczodata\\LCZO-ODM2-MariaTimeSeries3.sqlite'
loc = 'C:\\Users\\leonmi\\Desktop\\BoxUNH\\Box Sync\\data\\NEON\\lczodata\\LCZO-ODM2-MariaTimeSeries3.sqlite'
session_factory = dbconnection.createConnection('sqlite', loc)
dbsession = session_factory.getSession()

read = ReadODM2(session_factory)
write = CreateODM2(session_factory)

samplingfeatures = read.getSamplingFeatures()
samplingfeatureids = []
samplingfeaturenames = {}

for sf in samplingfeatures:
    print(sf)