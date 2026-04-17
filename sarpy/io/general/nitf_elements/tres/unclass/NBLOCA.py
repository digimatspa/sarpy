from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.utils import string_types

from builtins import super
from future import standard_library
standard_library.install_aliases()
from ..tre_elements import TREExtension, TREElement
import struct

__classification__ = "UNCLASSIFIED"
__author__ = "Thomas McCullough"


class FRAME(TREElement):
    def __init__(self, value):
        super(FRAME, self).__init__()
        self.add_field('FRAME_OFFSET', 'b', 4, value)


class NBLOCAType(TREElement):
    def __init__(self, value):
        super(NBLOCAType, self).__init__()
        self.add_field('FRAME_1_OFFSET', 'b', 4, value)
        self.add_field('NUMBER_OF_FRAMES', 'b', 4, value)
        self.add_loop('FRAMEs', struct.unpack('>I', self.NUMBER_OF_FRAMES)[0]-1, FRAME, value)


class NBLOCA(TREExtension):
    _tag_value = 'NBLOCA'
    _data_type = NBLOCAType
