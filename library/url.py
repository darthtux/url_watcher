# This module is a wrapper for communicating with TDAmeritrade and our local 
# python API host.  This is not meant to be called directly, but through 
# methods from other modules.  
import  json, sys, urllib.parse
from pathlib import Path
from urllib.request import Request, urlopen

class getURL():
    url = ''
    myHeaders = {}
    myData = {}
    returnCode = ''
    returnCodeText = ''
    parameters = ''

    def __init__(self, url):
        self.url = url
     
    def lookup(self):
        if(self.parameters == ''):
            print(self.url + self.parameters)
            api_call_data = Request(self.url, headers=self.myHeaders)
        else:
            print(self.url + self.parameters)
            api_call_data = Request(self.url + self.parameters, headers=self.myHeaders)

        with urlopen(api_call_data) as response:
            api_call_response = response.read()
            self.returnCode =  response.getcode()

        if(self.returnCode != 200):
            print('error: ' + str(api_call_response))  
            print(str(self.url) + str(self.parameters)) 
            self.returnCodeText = (api_call_response)
        
        self.myData = api_call_response

    def addParameter(self, myParameter, myValue):
        if (self.parameters == ''):
            self.parameters = '/?' + str(myParameter) + '=' + str(urllib.parse.quote(str(myValue)))
        else:
            self.parameters = str(self.parameters) + '&' +str(myParameter) + '=' + str(urllib.parse.quote(str(myValue)))

    def addHeader(self, myKey, myValue):
        self.myHeaders = self.myHeaders | {myKey : myValue}
