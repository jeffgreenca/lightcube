import unittest
import interface

class TestCubeMock(unittest.TestCase):
  def setUp(self):
    self.cube = interface.CubeMock()

  def test_invalid_output(self):
    self.assertFalse(self.cube.write("?"))

  def test_valid_output(self):
    self.assertTrue(self.cube.write("1"))
    
