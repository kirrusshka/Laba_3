import unittest
from file_job import *

class test(unittest.TestCase):
    def test_true(self):
        self.assertTrue(R("mama"))
        self.assertTrue(R("nn"))
        self.assertTrue(R("sestra"))

    def test_false(self):
        self.assertFalse(R("Kirill"))

    def test_probel_false(self):
        self.assertFalse(R("  "))
        self.assertFalse(R("ma pa"))
        self.assertFalse(R(""))