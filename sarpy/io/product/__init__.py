"""
This package contains the elements for interpreting product data.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.utils import string_types

from future import standard_library
standard_library.install_aliases()
__classification__ = 'UNCLASSIFIED'


def open(*args, **kwargs):
    from .converter import open_product
    return open_product(*args, **kwargs)
