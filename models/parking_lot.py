__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import copy

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
        self.__available_slots__ = set(slots)

    @property
    def occupied_slots(self):
        """
        :return: Returns a copy of `occupied_slots`
        """
        return copy.copy(self.__occupied_slots__)

    @property
    def available_slots(self):
        """
       :return: Returns a copy of `available_slots`
       """
        return copy.copy(self.__available_slots__)

    # Time complexity: O(1)
    def is_full(self):
        """
        Checks if there is any vacant slot available.
        """
        return len(self.__occupied_slots__) >= self.__size__

    def get_closest_slot(self):
        """
        Returns a closest(with minimum slot number) slot.
        :return:
        """
        if not self.__available_slots__:
            return None
        return min(self.__available_slots__)

    def get_slot_by_reg_num(self, reg_num):
        return self.__vehicle_slot_mapping__.get(reg_num, None)

    def is_slot_occupied(self, slot_number):
        return slot_number in self.__occupied_slots__

    def is_vehicle_parked(self, registration_number):
        """
        Checks if the vehicle with specified registration number is already parked.
        :param registration_number:
        """
        return registration_number in self.__vehicle_slot_mapping__

    def occupy_slot(self, slot, vehicle):
        """
        Reserves a `slot` for the `vehicle`
        :param slot: `Slot` to be reserved/occupied.
        :param vehicle: `Vehicle` to be parked.
        """
        self.__occupied_slots__[slot.slot_number] = vehicle.registration_number, vehicle.color
        self.__vehicle_slot_mapping__[vehicle.registration_number] = slot.slot_number
        self.__available_slots__.remove(slot)

    def vacate_slot(self, slot, reg_num):
        """
        Makes the `slot` free and available to be used by other vehicles.
        :param slot:
        :param reg_num: Vehicle registration number.
        """
        self.__occupied_slots__.pop(slot.slot_number)
        self.__vehicle_slot_mapping__.pop(reg_num)
        self.__available_slots__.add(slot)