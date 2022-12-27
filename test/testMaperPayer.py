import unittest

from validator import PeriodValidator


class PeriodValidatorTest(unittest.TestCase):

    def testPeriodValidatorTrue(self):
        vd = PeriodValidator("121990")
        self.assertTrue(vd.validate())

        vd = PeriodValidator("082020")
        self.assertTrue(vd.validate())

    def testPeriodValidatorFalse(self):
        vd = PeriodValidator("301990")
        self.assertFalse(vd.validate())
