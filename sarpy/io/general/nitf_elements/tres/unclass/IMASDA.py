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


class IMASDAType(TREElement):
    def __init__(self, value):
        super(IMASDAType, self).__init__()
        self.add_field('LONTR', 's', 22, value)
        self.add_field('LATTR', 's', 22, value)
        self.add_field('ELVTR', 's', 22, value)
        self.add_field('LONSC', 's', 22, value)
        self.add_field('LATSC', 's', 22, value)
        self.add_field('ELVSC', 's', 22, value)
        self.add_field('XITR', 's', 22, value)
        self.add_field('YITR', 's', 22, value)
        self.add_field('XISC', 's', 22, value)
        self.add_field('YISC', 's', 22, value)
        self.add_field('DELEV', 's', 22, value)


class IMASDA(TREExtension):
    _tag_value = 'IMASDA'
    _data_type = IMASDAType
