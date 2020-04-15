from hs_restclient import HydroShare, HydroShareAuthBasic

# Download LCZO sesnor database from Hydroshare
# link to the Hydroshare resource https://www.hydroshare.org/resource/b38bc00887ec45ac9499f9dea45eb8d5/

auth = HydroShareAuthBasic(username="miguelcleon", password = "x")
hs = HydroShare(auth = auth)
hs.getResource('b38bc00887ec45ac9499f9dea45eb8d5', destination='./lczodata', unzip=True)

