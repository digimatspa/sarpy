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


class CSPROAType(TREElement):
    def __init__(self, value):
        super(CSPROAType, self).__init__()
        self.add_field('RESERVED_0', 's', 12, value)
        self.add_field('RESERVED_1', 's', 12, value)
        self.add_field('RESERVED_2', 's', 12, value)
        self.add_field('RESERVED_3', 's', 12, value)
        self.add_field('RESERVED_4', 's', 12, value)
        self.add_field('RESERVED_5', 's', 12, value)
        self.add_field('RESERVED_6', 's', 12, value)
        self.add_field('RESERVED_7', 's', 12, value)
        self.add_field('RESERVED_8', 's', 12, value)
        self.add_field('BWC', 's', 12, value)


class CSPROA(TREExtension):
    _tag_value = 'CSPROA'
    _data_type = CSPROAType
