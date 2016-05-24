import unittest

import subprocess

class PartyTests(unittest.TestCase):
    """Tests for my auto_ssp.py"""

    def setUp(self):

         print("Begin Tests")

    def test_setup_build(self):

        build_app = "python setup.py py2app"
        result_code = subprocess.Popen(build_app, shell=True).wait()
        self.assertEqual(result_code, 0)


if __name__ == "__main__":
    unittest.main()