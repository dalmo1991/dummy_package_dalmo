import unittest
import sys
from os.path import abspath, join, dirname

import_folder = join(abspath(dirname(__file__)), '..', '..', 'dummy_package_dalmo')
sys.path.insert(0, import_folder)

from functions import sum

class TestSum(unittest.TestCase):

    def test_result(self):
        self.assertEqual(sum(2, 2), 5)

unittest.main()