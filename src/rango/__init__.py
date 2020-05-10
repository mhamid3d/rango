import os

try:
    version_filepath = os.path.join(__path__[0], "VERSION")
    with open(version_filepath) as version_file:
        __version__ = version_file.read().strip()
except IOError:
    pass
