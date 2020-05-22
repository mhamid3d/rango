import os
import logging
from rango.base.core import RangoHandler

LOGGER = logging.getLogger()
logging.basicConfig()

try:
    version_filepath = os.path.join(__path__[0], "VERSION")
    with open(version_filepath) as version_file:
        __version__ = version_file.read().strip()
except IOError:
    LOGGER.warning("Could not find 'VERSION' file in package directory. The __version__ attribute will be empty!")


def getHandler():
    return RangoHandler()
