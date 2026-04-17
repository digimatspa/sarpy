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


class GEOPSBType(TREElement):
    def __init__(self, value):
        super(GEOPSBType, self).__init__()
        self.add_field('TYP', 's', 3, value)
        self.add_field('UNI', 's', 3, value)
        self.add_field('DAG', 's', 80, value)
        self.add_field('DCD', 's', 4, value)
        self.add_field('ELL', 's', 80, value)
        self.add_field('ELC', 's', 3, value)
        self.add_field('DVR', 's', 80, value)
        self.add_field('VDCDVR', 's', 4, value)
        self.add_field('SDA', 's', 80, value)
        self.add_field('VDCSDA', 's', 4, value)
        self.add_field('ZOR', 's', 15, value)
        self.add_field('GRD', 's', 3, value)
        self.add_field('GRN', 's', 80, value)
        self.add_field('ZNA', 's', 4, value)


class GEOPSB(TREExtension):
    _tag_value = 'GEOPSB'
    _data_type = GEOPSBType
