import unittest
from unittest.mock import patch
import interface


class TestCubeMock(unittest.TestCase):
    def setUp(self):
        self.cube = interface.CubeMock()

    def test_invalid_output(self):
        self.assertFalse(self.cube.write("?"))

    def test_valid_output(self):
        self.assertTrue(self.cube.write("1"))


class TestCube(unittest.TestCase):
    @patch("serial.Serial")
    def setUp(self, Serial):
        self.cube = interface.Cube()

    def test_setup(self):
        self.cube.com.write.assert_called_with(b"x")

    def test_valid_input(self):
        self.cube.com.write.reset_mock()
        self.assertTrue(self.cube.write("1"))
        self.cube.com.write.assert_called_once_with(b"1")

    def test_invalid_input(self):
        self.cube.com.write.reset_mock()
        self.assertFalse(self.cube.write("?"))
        self.cube.com.write.assert_not_called()
