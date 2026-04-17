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


class OFFSETType(TREElement):
    def __init__(self, value):
        super(OFFSETType, self).__init__()
        self.add_field('LINE', 's', 8, value)
        self.add_field('SAMPLE', 's', 8, value)


class OFFSET(TREExtension):
    _tag_value = 'OFFSET'
    _data_type = OFFSETType
