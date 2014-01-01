#!/usr/bin/python
from pyMetascanAPI import pyMetascanAPI
import os

api_key = '42c00f42f044947a5870dacbe02e6539'

file = os.getcwd() + '/test_file.txt'
data_id = '548f59618bd543e89d8d71ed5fb1f745'
hash = '098F6BCD4621D373CADE4E832627B4F6'

pyMetascan = pyMetascanAPI(api_key)

print pyMetascan.fileUpload(file)
print pyMetascan.retrieveReport(data_id)
print pyMetascan.hashLookup(hash)
