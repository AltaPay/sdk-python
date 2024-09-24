#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Terminals test script.

"""

import sys, random

# Update this with real path and uncomment before use, please
# sys.path.append('/absolute_path_to/python-client-library')

#sdk path check
sdkPathExists = False
for path in sys.path:
    if path.endswith("/sdk-python"):
        sdkPathExists=True
if sdkPathExists is False:
    print("Path to sdk-python does not exist, update your environment variable, or put sys.path.append('/absolute_path_to/sdk-python') before including altapay sdk modules")
    sys.exit()

from altapay import API, Terminals

api = API(mode='test',account='API username', password='API Password',  url='https://testgateway.altapaysecure.com/merchant/')

response=Terminals(api=api)

print(response.terminals)
