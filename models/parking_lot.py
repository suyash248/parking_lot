__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

class ParkingLot(object):
    """
    Instance of this class represents the parking lot.
    """
    def __init__(self, size, slots=()):
        """
        :param size: Number of vehicles that can be parked in the parking lot. i.e. `capacity`.

        :param slots: Sequence of `models.slot.Slot` instances.
        """
        self.__size__ = size
        self.__occupied_slots__ = dict()
        self.__vehicle_slot_mapping__ = dict()
        self.__available_slots__ = list(slots)