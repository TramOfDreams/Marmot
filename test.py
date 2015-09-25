#!/usr/bin/env python

import unittest
from marmot import Marmot, MarmotList


class TestMarmot(unittest.TestCase):
    def setUp(self):
        self.m = Marmot('sony')
  
    def test_name(self):
        self.assertTrue(self.m.name, 'sony')

    def test_marmot_behaviour(self):
        # Feed the Marmot.
        self.m.feed('beer')
        self.m.feed('beer')
        self.m.feed('nut')

        # Whistle test.
        self.assertTrue(self.m.whistle())
        self.assertTrue(self.m.whistle())
        self.assertTrue(self.m.whistle())
        self.assertFalse(self.m.whistle())


class TestMarmotList(TestMarmot):
    def setUp(self):
        self.m = MarmotList('sony')

if __name__ == '__main__':
    unittest.main() 
