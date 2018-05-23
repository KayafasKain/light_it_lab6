import unittest
from unittest import mock
from unittest.mock import patch
import greeter
import logging
import datetime

class GreeterTestCase(unittest.TestCase):

    def test_greet(self):
        test_str = "Hello, pony"
        name = "pony"
        obj = greeter.Greeter()
        self.assertEqual( obj.greet(name), test_str)

    def test_greet_second(self):
        test_str = "Hello, pony"
        enter = "     pony    "
        obj = greeter.Greeter()
        self.assertEqual( obj.greet(enter), test_str )

    def test_greet_third(self):
        test_str = "Hello, pony"
        enter = "pony"
        obj = greeter.Greeter()
        self.assertEqual(obj.greet(enter), test_str)

    @patch("greeter.logging")
    @patch("greeter.datetime")
    def test_greet_fourth(self, mock_dt, mock_logger):
        mock_dt.now.return_value = 9
        obj = greeter.Greeter()
        name = "pony"
        test_str = "Good morning, pony"
        self.assertEqual(obj.greet_time(name), test_str)

    @patch("greeter.logging")
    @patch("greeter.datetime")
    def test_greet_five(self, mock_dt, mock_logger):
        mock_dt.now.return_value = 19
        obj = greeter.Greeter()
        name = "pony"
        test_str = "Good evening, pony"
        mock_logger.logger.info(test_str)
        mock_logger.logger.info.assert_called_with(obj.greet_time(name))
        self.assertEqual(obj.greet_time(name), test_str)

    @patch("greeter.logging")
    @patch("greeter.datetime")
    def test_greet_six(self, mock_dt, mock_logger):
        mock_dt.now.return_value = 23
        obj = greeter.Greeter()
        name = "pony"
        test_str = "Good night, pony"
        mock_logger.logger.info(test_str)
        mock_logger.logger.info.assert_called_with(obj.greet_time(name))
        self.assertEqual(obj.greet_time(name), test_str)


if __name__ == '__main__':
    unittest.main()

