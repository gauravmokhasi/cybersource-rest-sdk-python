import json
import sys
sys.path.append('../src/Api')
from CaptureApi import CaptureApi 

import os
import unittest
if sys.version_info < (3, 0):
    import ConfigParser as parser
else:
    import configparser as parser

class TestCybersourcePayment(unittest.TestCase):
    
    config = parser.ConfigParser()
    config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'../','configuration.ini'))
    config.read(config_path)

    def setUp(self):
        self.paymentAuthorizationRequest = ''
        with open('./samples/refund.json','r') as refundPayLoad:
            self.paymentAuthorizationRequest = json.loads(refundPayLoad.read())
        print(self.paymentAuthorizationRequest)
        self.visaApiClient = CaptureApi(self.paymentAuthorizationRequest)
    
    def test_cybersource_payment_authorization(self):
        query_string = 'apikey=' + self.config.get('VDP','apiKey')
        response = self.visaApiClient.refund("capture_id")
        print(response.text)
        pass

test = TestCybersourcePayment()
test.setUp()
test.test_cybersource_payment_authorization()
