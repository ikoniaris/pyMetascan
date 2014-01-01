import requests
import os

class pyMetascanAPI:
    API_ENDPOINT = 'https://api.metascan-online.com/v1/'
    API_KEY = ''

    FILE_EXT = 'file'
    DATA_EXT = 'file/'
    HASH_EXT = 'hash/'

    def __init__(self, api_key):
        self.API_KEY = api_key

    def fileUpload(self, file):
        r = self.makeRequest(self.getFileEndpoint(), 'POST', file)
        return r.json()

    def retrieveReport(self, data_id):
        r = self.makeRequest(self.getDataEndpoint(data_id))
        return r.json()

    def hashLookup(self, hash):
        r = self.makeRequest(self.getHashEndpoint(hash))
        return r.json()

    def makeRequest(self, url, method='GET', file=None):
        headers = {'apikey' : self.API_KEY}

        if method == 'POST':
            headers.update({'filename' : os.path.basename(file)})
            return requests.post(url, file, headers=headers)
        else:
            return requests.get(url, headers=headers)

    def getFileEndpoint(self):
        return self.API_ENDPOINT + self.FILE_EXT

    def getDataEndpoint(self, data_id):
        return self.API_ENDPOINT + self.DATA_EXT + data_id

    def getHashEndpoint(self, hash):
        return self.API_ENDPOINT + self.HASH_EXT + hash
