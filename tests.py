#!/usr/bin/python
# -*- coding: utf8 -*-

"""This is the test suite for testing the server script. To execute the tests:
    ./tests.py
"""
import unittest

from base64 import b64encode
from server import get_number_of_value_crossings, app


class TestNumberOfValueCrossings(unittest.TestCase):

    def setUp(self):
        self.func = get_number_of_value_crossings


    def test_normal_signal(self):
        """Test normal signal"""
        signal = [4,1,2,6,5,4,7,8,9,5,6,4,2,3,1,0,2,1,9,7,5,2,0,1,5,5,5,2,5,5,3,8,9,7,4,1,1]
        value = 5
        self.assertEqual(self.func(signal, value), 8)

    def test_negative_signal(self):
        """Test signal with negative values"""
        signal = [-4,-1,-2,-6,-5,-4,-7,-8,-9,-5,-6,-4,-2,-3,-1,-0,-2,-1]
        value = -5
        self.assertEqual(self.func(signal, value), 4)

    def test_high_value(self):
        """Test high value"""
        signal = [-4,-1,-2,-6,-5,-4,-7,-8,-9,-5,-6,-4,-2,-3,-1,-0,-2,-1]
        value = 5
        self.assertEqual(self.func(signal, value), 0)

    def test_low_value(self):
        """Test low value"""
        signal = [-4,-1,-2,-6,-5,-4,-7,-8,-9,-5,-6,-4,-2,-3,-1,-0,-2,-1]
        value = -50
        self.assertEqual(self.func(signal, value), 0)


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def get_header(self, username, password):
        all_cred = "{0}:{1}".format(username, password)
        encode_all = b64encode(all_cred.encode('ascii')).decode()
        return {
            'Authorization': 'Basic {0}'.format(encode_all)
        }

    def test_http_200(self):
        """Test 200 OK standard response for successful HTTP"""
        rsps = self.app.post('/',
                                 data={'signal':'4,5,6,8,3,5,-2,4,-1','value':'5'},
                                 headers=self.get_header('evan', 'python3'))
        self.assertEqual(rsps.status_code, 200)
        self.assertEqual(rsps.data.decode(), '{"crossing_number": 2}')

    def test_http_404(self):
        """Test 404 Not Found"""
        rsps = self.app.post('/not_existed/',
                                 data={'signal':'4,5,6,8,3,5,-2,4,-1','value':'5'},
                                 headers=self.get_header('evan', 'python3'))
        self.assertEqual(rsps.status_code, 404)
        self.assertNotEqual(rsps.data.decode(), '{"crossing_number": 2}')

    def test_http_401(self):
        """Test 401 Unauthorized"""
        rsps = self.app.post('/',
                                 data={'signal':'4,5,6,8,3,5,-2,4,-1','value':'5'},
                                 headers=self.get_header('evan', 'INVALID'))
        self.assertEqual(rsps.status_code, 401)
        self.assertNotEqual(rsps.data.decode(), '{"crossing_number": 2}')

    def test_http_422_no_signal(self):
        """Test 422 Unprocessable Entity"""
        rsps = self.app.post('/',
                                 data={'value':'5'},
                                 headers=self.get_header('evan', 'python3'))
        self.assertEqual(rsps.status_code, 422)
        self.assertNotEqual(rsps.data.decode(), '{"crossing_number": 2}')

    def test_http_422_no_signal_content(self):
        """Test 422 Unprocessable Entity"""
        rsps = self.app.post('/',
                                 data={'signal':'', 'value':'5'},
                                 headers=self.get_header('evan', 'python3'))
        self.assertEqual(rsps.status_code, 422)
        self.assertNotEqual(rsps.data.decode(), '{"crossing_number": 2}')

    def test_http_422_invalid_signal_content(self):
        """Test 422 Unprocessable Entity"""
        rsps = self.app.post('/',
                                 data={'signal':'INVALID CONTENT', 'value':'5'},
                                 headers=self.get_header('evan', 'python3'))
        self.assertEqual(rsps.status_code, 422)
        self.assertNotEqual(rsps.data.decode(), '{"crossing_number": 2}')

    def test_http_422_invalid_value_content(self):
        """Test 422 Unprocessable Entity"""
        rsps = self.app.post('/',
                                 data={'signal':'4,5,6,8,3,5,-2,4,-1', 'value':'INVALID CONTENT'},
                                 headers=self.get_header('evan', 'python3'))
        self.assertEqual(rsps.status_code, 422)
        self.assertNotEqual(rsps.data.decode(), '{"crossing_number": 2}')

if __name__ == '__main__':
    unittest.main()
