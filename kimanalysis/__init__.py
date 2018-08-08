"""
Attributes
----------
__version__ : str
    The package version.
"""
# Standard Python libraries
from __future__ import division, absolute_import, print_function
import os

# Read version from VERSION file
with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

from . import compatibility
from . import unitconvert
from .alloweditemtype import *
from .rawquery import rawquery
from .kimids import *

from .listids import listids
from .getitem import getitem
from .queryitems import queryitems
from .queryresults import queryresults
from .getbibliography import getbibliography
from .getfile import getfile
from .getallfiles import getallfiles
from .listfiles import listfiles