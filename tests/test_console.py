import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual(f.getvalue().strip(), "")

    # Add more test cases for other commands such as "create", "show", "destroy", etc.

if __name__ == '__main__':
    unittest.main()
