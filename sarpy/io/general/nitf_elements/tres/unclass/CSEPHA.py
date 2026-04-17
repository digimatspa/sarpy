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


class EPHEM(TREElement):
    def __init__(self, value):
        super(EPHEM, self).__init__()
        self.add_field('EPHEM_X', 's', 12, value)
        self.add_field('EPHEM_Y', 's', 12, value)
        self.add_field('EPHEM_Z', 's', 12, value)


class CSEPHAType(TREElement):
    def __init__(self, value):
        super(CSEPHAType, self).__init__()
        self.add_field('EPHEM_FLAG', 's', 12, value)
        self.add_field('DT_EPHEM', 's', 5, value)
        self.add_field('DATE_EPHEM', 's', 8, value)
        self.add_field('T0_EPHEM', 's', 13, value)
        self.add_field('NUM_EPHEM', 'd', 3, value)
        self.add_loop('EPHEMs', self.NUM_EPHEM, EPHEM, value)


class CSEPHA(TREExtension):
    _tag_value = 'CSEPHA'
    _data_type = CSEPHAType
