"""
**This sub-package is a work in progress to encapsulate pythonic object-oriented SICD structure 1.1 (2014-09-30).**

This purpose of doing it this way is to encourage effective documentation and streamlined use of the SICD information.
This provides more robustness than using structures with no built-in validation, and more flexibility than using the
rigidity of C++ based standards validation.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.utils import string_types

from future import standard_library
standard_library.install_aliases()
__classification__ = "UNCLASSIFIED"
