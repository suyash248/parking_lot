__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from collections import namedtuple

__SizeInfo__ = namedtuple("__SizeInfo__", "key")

class VehicleSize(object):
    SMALL = __SizeInfo__(key="small")
    MEDIUM = __SizeInfo__(key="medium")
    LARGE = __SizeInfo__(key="large")