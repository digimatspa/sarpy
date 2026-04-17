"""
This package contains the AFRL RDE schema
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.utils import string_types

from future import standard_library
standard_library.install_aliases()
__classification__ = 'UNCLASSIFIED'

import pkg_resources


def get_schema_path(version='1.0.0'):
    """
    Location of AFRL/RDE schema file.

    Returns
    -------
    str
        The path to the ARFL/RDE schema.
    """

    if version == '1.0.0':
        return pkg_resources.resource_filename(
            'sarpy.annotation.afrl_rde_schema', 'afrl_rde_schema_v1.0.0_2022-02-15.xsd')
    else:
        raise ValueError('Got unrecognized version {}'.format(version))
