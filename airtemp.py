# "dataProductCode": "DP1.00003.001",
#         "dataProductTitle": "Triple aspirated air temperature",

import requests
import json
import csv
import urllib.request

# download air temperature data for Guanica Forest from NEON REST API

SITECODE = "GUAN" #the site code for Guanica forest
# http://data.neonscience.org/data-product-view?dpCode=DP1.00003.001
PRODUCTCODE = "DP1.00003.001" #the product code for air temperature


SERVER = "http://data.neonscience.org/api/v0/" #the current server address

site_response = requests.get(SERVER + 'sites/' + SITECODE)


site_response_json = site_response.json()
data_products = site_response_json['data']['dataProducts']
months=[]

for data_product in data_products:
    if (data_product['dataProductCode'] == PRODUCTCODE):
        print(data_product)
        months = data_product['availableMonths']

print(months)

x =site_response_json

for key,val in x.items():
    print(key)
    print(val)
    code = None
    title = None
    months = None
    urls = None
    for key3,val3 in val.items():
        print(key3)
        print(val3)
        if key3 == 'dataProducts':
            for listitem in val3:
                for key2, val2 in listitem.items():
                    if key2 == 'dataProductCode':
                        code = val2
                    if key2 == 'dataProductTitle':
                        title = val2
                        if title == 'Triple aspirated air temperature':
                            print(title)
                    if key2 == 'availableMonths':
                        months = val2
                    if key2 == 'availableDataUrls':
                        urls = val2
                        if title == 'Triple aspirated air temperature':
                            print(urls)
                            i=0
                            for url in urls:

                                print(url)
                                # urllib.request.urlretrieve(url, '/airtemp/temp' + str(i) + '.json')
                                with urllib.request.urlopen(url) as morejson:
                                    data = json.loads(morejson.read().decode())
                                    print(data)
                                    for key4, val4 in data.items():
                                        print(key4)
                                        print(val4)
                                        # TAAT_30min
                                        for key5, val5 in val4.items():
                                            print(key5)
                                            print(val5)
                                            if key5 == 'files':
                                                for listitem2 in val5:
                                                    url = ''
                                                    name = ''
                                                    for key6, val6 in listitem2.items():
                                                        print(key6)
                                                        print(val6)
                                                        if key6 == 'url' and 'TAAT_30min' in val6:
                                                            url = val6
                                                        if key6 == 'name' and 'TAAT_30min' in val6:
                                                            name = val6
                                                    if len(url) > 0:
                                                        print(url)
                                                        urllib.request.urlretrieve(url, './airtemp/' + name)
