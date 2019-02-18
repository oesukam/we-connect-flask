import unittest

def add(a=0, b=0):
  return a + b

class TestSample(unittest.TestCase):
  def test_add(self):
    result = add(2, 3)
    self.assertEqual(result, 5)