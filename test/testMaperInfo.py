import unittest

from maper.maperInfo import DataValidator


class TestDataValidator(unittest.TestCase):

    def testDataValidTrue(self):
        dv = DataValidator("10.12.2020")
        self.assertTrue(dv.validate())

    def testDataValidFalse(self):
        dv = DataValidator("10.19.2020")
        self.assertFalse(dv.validate())

    def testRangeDataValidFalse(self):
        dv = DataValidator("10.19.2020")
        self.assertFalse(dv._range_validate())
        dv.date = "40.09.2020"
        self.assertFalse(dv._range_validate())