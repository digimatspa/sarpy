"""
Types implementing the SIDD 3.0 DigitalElevationData Parameters
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.utils import string_types
from future import standard_library
standard_library.install_aliases()
__classification__ = 'UNCLASSIFIED'

# SIDD 3.0 reuses the SIDD 2.0 types.  Make those symbols available in this module.
from sarpy.io.product.sidd2_elements.DigitalElevationData import (
    GeographicCoordinatesType,
    GeopositioningType,
    AccuracyType,
    PositionalAccuracyType,
    DigitalElevationDataType,
)

__REUSED__ = (  # to avoid unused import lint errors
    GeographicCoordinatesType,
    GeopositioningType,
    AccuracyType,
    PositionalAccuracyType,
    DigitalElevationDataType,
)
