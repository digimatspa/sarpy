from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.utils import string_types

from builtins import super
from future import standard_library
standard_library.install_aliases()
from ..tre_elements import TREExtension, TREElement

__classification__ = "UNCLASSIFIED"
__author__ = "Thomas McCullough"


class CSCRNAType(TREElement):
    def __init__(self, value):
        super(CSCRNAType, self).__init__()
        self.add_field('PREDICT_CORNERS', 's', 1, value)
        self.add_field('ULCNR_LAT', 's', 9, value)
        self.add_field('ULCNR_LONG', 's', 10, value)
        self.add_field('ULCNR_HT', 's', 8, value)
        self.add_field('URCNR_LAT', 's', 9, value)
        self.add_field('URCNR_LONG', 's', 10, value)
        self.add_field('URCNR_HT', 's', 8, value)
        self.add_field('LRCNR_LAT', 's', 9, value)
        self.add_field('LRCNR_LONG', 's', 10, value)
        self.add_field('LRCNR_HT', 's', 8, value)
        self.add_field('LLCNR_LAT', 's', 9, value)
        self.add_field('LLCNR_LONG', 's', 10, value)
        self.add_field('LLCNR_HT', 's', 8, value)


class CSCRNA(TREExtension):
    _tag_value = 'CSCRNA'
    _data_type = CSCRNAType
