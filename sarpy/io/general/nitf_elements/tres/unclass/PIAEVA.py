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


class PIAEVAType(TREElement):
    def __init__(self, value):
        super(PIAEVAType, self).__init__()
        self.add_field('EVENTNAME', 's', 38, value)
        self.add_field('EVENTTYPE', 's', 8, value)


class PIAEVA(TREExtension):
    _tag_value = 'PIAEVA'
    _data_type = PIAEVAType
