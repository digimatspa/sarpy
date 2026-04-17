from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.utils import string_types
from future import standard_library
standard_library.install_aliases()
from .__about__ import *
import logging


__all__ = ['__version__',
           '__classification__', '__author__', '__url__', '__email__',
           '__title__', '__summary__',
           '__license__', '__copyright__']


# establish logging paradigm
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
