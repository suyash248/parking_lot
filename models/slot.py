__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

class Slot(object):
    """
    Represents a parking slot.
    """
    def __init__(self, slot_number):
        self.slot_number = int(slot_number)

    def __str__(self):
        return str(self.slot_number)

    def __repr__(self):
        return str(self.slot_number)

    def __le__(self, other):
        return self.slot_number <= other.slot_number

    def __lt__(self, other):
        return self.slot_number < other.slot_number

    def __ge__(self, other):
        return self.slot_number >= other.slot_number

    def __gt__(self, other):
        return self.slot_number > other.slot_number

    def __eq__(self, other):
        return self.slot_number == other.slot_number

    def __ne__(self, other):
        return self.slot_number != other.slot_number
