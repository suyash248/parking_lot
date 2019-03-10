__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from collections import namedtuple

__SizeInfo__ = namedtuple("__SizeInfo__", "key")
class VehicleSize(object):
    SMALL = __SizeInfo__(key="small")
    MEDIUM = __SizeInfo__(key="medium")
    LARGE = __SizeInfo__(key="large")

class Command(object):
    """
    Member of this class represents a valid command.
    """
    CREATE = 'CREATE'
    PARK = 'PARK'
    LEAVE = 'LEAVE'
    STATUS = 'STATUS'
    REG_NUMS_BY_COLOR = 'REG_NUMS_BY_COLOR'
    SLOT_NUMS_BY_COLOR = 'SLOT_NUMS_BY_COLOR'
    SLOT_NUM_BY_REG_NUM = 'SLOT_NUM_BY_REG_NUM'

_PatternInfo_ = namedtuple('_PatternInfo_', 'pattern groups')

# Command-to-Regex_pattern mapping.
CMD_REGEX_PATTERNS = {
    Command.CREATE: _PatternInfo_(r"^(?P<cmd>create_parking_lot)\s+(?P<size>\d+)\s*$",
                            ('cmd', 'size')),
    Command.PARK: _PatternInfo_(r"^(?P<cmd>park)\s+(?P<reg_num>.+[^\s])\s+(?P<color>\w+)\s*$",
                            ('cmd', 'reg_num', 'color')),
    Command.LEAVE: _PatternInfo_(r"^(?P<cmd>leave)\s+(?P<slot_num>\d+)\s*$",
                            ('cmd', 'slot_num')),
    Command.STATUS: _PatternInfo_(r"^(?P<cmd>status)\s*$", ('cmd',)),
    Command.REG_NUMS_BY_COLOR: _PatternInfo_(r"^(?P<cmd>registration_numbers_for_cars_with_colour)\s+(?P<color>\w+)\s*$",
                            ('cmd', 'color')),
    Command.SLOT_NUMS_BY_COLOR: _PatternInfo_(r"^(?P<cmd>slot_numbers_for_cars_with_colour)\s+(?P<color>\w+)\s*$",
                            ('cmd', 'color')),
    Command.SLOT_NUM_BY_REG_NUM: _PatternInfo_(r"^(?P<cmd>slot_number_for_registration_number)\s+(?P<reg_num>.+[^\s])\s*$",
                            ('cmd', 'reg_num'))
}

_ColorInfo_ = namedtuple("_ColorInfo_", "name hex")
class Color(object):
    """
    Enum of popular colors. (But as of now, we don't have a predefined list of colors so can't use it.)
    """
    WHITE = _ColorInfo_('white', '#FFFFFF')
    BLACK = _ColorInfo_('black', '#000000')
    RED = _ColorInfo_('red', '#ED2939')
    BLUE = _ColorInfo_('blue', '#0000FF')
    GREEN = _ColorInfo_('green', '#008000')
    YELLOW = _ColorInfo_('yellow', '#FFFF33')

class Response(object):
    def __init__(self, success=True, message="", data=None, error=None):
        self.success = success
        self.message = message
        self.data = data
        self.error = error

    @property
    def to_dict(self):
        return dict(sucess=self.success, message=self.message, data=self.data, error=self.error)

class ErrorConstant(object):
    INVALID_COMMAND = 'INVALID_COMMAND'
    NO_PARKING_LOT_FOUND = 'NO_PARKING_LOT_FOUND'
    PARKING_LOT_OVERFLOW = 'PARKING_LOT_OVERFLOW'
    SLOT_OCCUPIED = 'SLOT_OCCUPIED'
    VEHICLE_IS_ALREADY_PARKED = 'VEHICLE_IS_ALREADY_PARKED'
    INVALID_SLOT = 'INVALID_SLOT'
    INVALID_REGISTRATION_NUMBER = 'INVALID_REGISTRATION_NUMBER'