import requests
import json
import csv

SITECODE = "GUIL" #the site code for Abby Road
# http://data.neonscience.org/data-product-view?dpCode=DP1.00036.001
PRODUCTCODE = "DP4.00200.001" #the product code for eddy covariance data product (DP4.00200.001).

#http://data.neonscience.org/data-product-view?dpCode=DP4.00200.001
SERVER = "http://data.neonscience.org/api/v0/" #the current server address

site_response = requests.get(SERVER + 'sites/' + SITECODE)


site_response_json = site_response.json()
print(json.dumps(site_response_json, indent=2)) #using json.dumps for formatting



data_products = site_response_json['data']['dataProducts']
months=[]
#use a list comprehension here if you're feeling fancy
for data_product in data_products:
    if (data_product['dataProductCode'] == PRODUCTCODE):
        months = data_product['availableMonths']

print(months)

x =site_response_json
f = csv.writer(open('GuilavailableNEONdata.csv','w+', newline='\n'))

f.writerow(['data product code', 'data product title', 'available months', 'urls'])
for key,val in x.items():
    print(key)
    code = None
    title = None
    months = None
    urls = None
    for key3,val3 in val.items():
        print(key3)
        if key3 == 'dataProducts':
            print('HERE HERE')
            print(val3)
            for listitem in val3:
                for key2, val2 in listitem.items():
                    if key2 == 'dataProductCode':
                        code = val2
                    if key2 == 'dataProductTitle':
                        title = val2
                    if key2 == 'availableMonths':
                        months = val2
                    if key2 == 'availableDataUrls':
                        urls = val2
                    if code and title and months and urls:
                        f.writerow([code,title,months,urls])
                        code = None
                        title = None
                        months = None
                        urls = None