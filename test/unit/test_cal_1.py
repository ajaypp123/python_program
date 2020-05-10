#!/usr/bin/env python3

import unittest

class Cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def  sub(self):
        return self.a - self.b

class TestCal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Initial Setup')

    @classmethod
    def tearDownClass(cls):
        print('Teardown Class')

    def setUp(self):
        print('setUp')
        self.cal = Cal(4,2)

    def tearDown(self):
        print('tearDown')
        self.cal = None

    def test_add(self):
        print('add')
        self.assertEqual(self.cal.add(), 6)

    def test_sub(self):
        print('sub')
        self.assertEqual(self.cal.sub(), 2)

if __name__ == '__main__':
    unittest.main()