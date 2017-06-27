#!/usr/bin/python
# -*- coding: utf8 -*-

"""This is the test suite for testing the server script. To execute the tests:
    ./tests.py
"""
import os
import unittest
import signal

from server import get_number_of_value_crossings


class TestNumberOfValueCrossings(unittest.TestCase):

    def setUp(self):
        self.func = get_number_of_value_crossings

    def tearDown(self):
        # Kill the process
        pass

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

    #TODO run the curl commands

if __name__ == '__main__':
    unittest.main()
