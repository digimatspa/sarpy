from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.utils import string_types

from future import standard_library
standard_library.install_aliases()
import numpy

__author__ = "Thomas McCullough"
__classification__ = "UNCLASSIFIED"


def argument_validation(lat, lon):
    if not isinstance(lat, numpy.ndarray):
        lat = numpy.array(lat)
    if not isinstance(lon, numpy.ndarray):
        lon = numpy.array(lon)
    if lat.shape != lon.shape:
        raise ValueError(
            'lat and lon must have the same shape, got '
            'lat.shape = {}, lon.shape = {}'.format(lat.shape, lon.shape))
    o_shape = lat.shape
    lat = numpy.reshape(lat, (-1,))
    lon = numpy.reshape(lon, (-1,))

    return o_shape, lat, lon
