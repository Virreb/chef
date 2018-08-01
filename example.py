# -*- coding: utf-8 -*-
import requests
import time

#from api_functions import generate_random_token
#print('random token: ', generate_random_token())

uri_host = 'https://ess-group-customer-api.eu-de.mybluemix.net'
#uri_host = 'http://0.0.0.0:5000'
uri_prefix = '/api/v1.0'
token0 = 'KvYQEhC3i70SgS_2AD6wmHG1cKo'   # Advectas access
token1 = 'TlbAyUvRhM71MwnFvHygZtCiWQ8'   # Ess group access
token2 = 'XwKhrwRACPNJY7xcUYa3kjqGXRA'  # Book visit access

# Check if customer exists
p0 = 'hej'
p1 = '20121212-1111'
p2 = '19520229-4335'

# post updates to DB
start_time1 = time.time()
request_uri = uri_host + uri_prefix + '/customer'
params = {'C_PERSONNR': p1, 'C_GIVENNAME': 'Donko', 'C_LASTNAME': 'Bronko', 'C_PHONE': '+46733221100',
          'C_EMAIL': 'donko@bronko.com', 'C_REGISTERED_ADDRESS': 'Stora gatan 2', 'C_CLEAN_DATE': '2017-01-13 12:31:45',
          'C_ZIP': '12345', 'C_CITY': 'Storstan', 'C_KOMMUN': 'Kranskommunen', 'C_LAN': 'VGR och Värmlands län',
          'C_COUNTRY': 'Schweden', 'ISOCODE': 'SE', 'MEMBER_DATE': '2017-01-12 22:14:33', 'MEMBER': 1,
          'FAV_HOTEL': 'Hotel1, hotel2', 'ENROL_CHANNEL': 'Facebook', 'B2B_INFO': 1, 'ENROL_HOTEL': 'Hotel1',
          'USED_CAMPAIGN': 'abc123',
          'token': token0}
#params2 = {'C_PERSONNR': p1, 'C_GIVENNAME': 'Vicktor', 'C_LASTNAME': 'Bachmann', 'token': token1}
r = requests.put(request_uri, params=params)
print('put: ', r.status_code, r.json(), 'comp. time: ', time.time()-start_time1)

start_time2 = time.time()
# read if the updates worked
params = {'C_PERSONNR': p1, 'token': token0}
r = requests.get(request_uri, params=params)

print('get: ', r.status_code, r.json())
print('Comp. time:', time.time() - start_time2)
