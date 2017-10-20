#!/usr/bin/env python

import unittest
from Main import extract_commands

class testExtractCmd(unittest.TestCase):

    def setUp(self):
        pass

    def test_extract_cmd(self):
        self.assertRaises(AssertionError,extract_commands,['FAIL'])
        self.assertRaises(AssertionError, extract_commands,['PLACE'])
        self.assertRaises(AssertionError, extract_commands,['PLACE','0'])
        self.assertRaises(AssertionError, extract_commands,['PLACE','0,100,NORTH'])
        self.assertRaises(AssertionError, extract_commands,['PLACE','0,1,NORTH','FAIL'])

if __name__ == '__main__':
    unittest.main()
