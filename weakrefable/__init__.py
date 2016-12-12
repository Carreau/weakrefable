"""
Determined whether an object can be weakref'd
"""

version_info = (0,0,1)
__version__ = '.'.join([str(x) for x in version_info])

from _weakrefable import canbeweakreferenced
