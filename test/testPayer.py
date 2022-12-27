import unittest

from ODT import Payer


class TestPayer(unittest.TestCase):

    def testEqualHash(self):
        p1 = Payer(
            personal_account="123",
            period="012020"
        )

        p2 = Payer(
            personal_account="123",
            period="012020",
            total=100
        )

        self.assertEqual(hash(p1), hash(p2))
