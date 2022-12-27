import unittest

from validator import DateValidator


class TestDataValidator(unittest.TestCase):

    def testDataValidTrue(self):
        dv = DateValidator("10.12.2020")
        self.assertTrue(dv.validate())

    def testDataValidFalse(self):
        dv = DateValidator("10.19.2020")
        self.assertFalse(dv.validate())

    def testRangeDataValidFalse(self):
        dv = DateValidator("10.19.2020")
        self.assertFalse(dv._range_validate())
        dv.date = "40.09.2020"
        self.assertFalse(dv._range_validate())
