try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib

import pytest
try:
    import unittest2 as unittest
except ImportError:
    import unittest

if not hasattr(unittest.TestCase, 'assertRaisesRegex'):
    unittest.TestCase.assertRaisesRegex = unittest.TestCase.assertRaisesRegexp

@pytest.fixture
def tests_path():
    return pathlib.Path(__file__).parent
