from util.constants import Response, ErrorConstant

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from models.slot import SmallSlot
from models.parking_lot import ParkingLot

class ParkingService(object):

    def __init__(self, parking_lot=None):
        self._parking_lot_ = parking_lot

    @property
    def parking_lot(self):
        return self._parking_lot_

    @parking_lot.setter
    def parking_lot(self, parking_lot):
        self._parking_lot_ = parking_lot

    def create_parking_lot(self, size, slots=()):
        slots = slots or list(map(SmallSlot, range(1, size+1)))
        self.parking_lot = ParkingLot(size, slots=slots)

    def park(self, vehicle):
        """
        Allocate(if available) a `slot` to the `vehicle`.

        :param vehicle: Instance of class:`Vehicle<models.vehicle.Vehicle>`.

        :return: Allocated `slot_number` wrapped under `util.constants.Response` object.
        """
        response = Response()
        if self.parking_lot.is_full():
            # parking lot is full.
            return Response(success=False, error=ErrorConstant.PARKING_LOT_OVERFLOW)

        slot = self.parking_lot.get_closest_slot()
        if slot is None:
            # parking lot is full.
            return Response(success=False, error=ErrorConstant.PARKING_LOT_OVERFLOW)

        if self.parking_lot.is_slot_occupied(slot.slot_number):
            # Slot is already occupied by another vehicle.
            return Response(success=False, error=ErrorConstant.SLOT_OCCUPIED)
        if self.parking_lot.is_vehicle_parked(vehicle.registration_number):
            # This vehicle is already parked.
            return Response(success=False, error=ErrorConstant.VEHICLE_IS_ALREADY_PARKED)

        self.parking_lot.occupy_slot(slot, vehicle)
        return Response(data={'slot_num': slot.slot_number})

    # Time complexity: O(log(n))
    def leave(self, slot):
        """
        Makes a `slot` free & ready to be used again.

        :param slot:
        :return: `registration_number` of the vehicle, which has just left, wrapped under `util.constants.Response` object.
        """

        reg_num, color = self.parking_lot.occupied_slots.get(slot.slot_number, (None, None))
        if reg_num is None:
            # Slot is not occupied
            return Response(success=False, error=ErrorConstant.INVALID_SLOT)
        self.parking_lot.vacate_slot(slot, reg_num)
        return Response(data={'reg_num': reg_num})

    # Time complexity: O(n-m), m: number of available/vacant slots.
    def status(self):
        """
        :return: Returns a tuple of `slot_number`, `registration_number`, `color`.
        """
        for slot_num, (reg_num, col) in self.parking_lot.occupied_slots.items():
            yield slot_num, reg_num, col.capitalize()

    def slot_numbers_by_color(self, color):
        """
        Yields the `slot_number`, if the vehicle occupying the slot has a specific color.

        :param color:
        """
        color = color.strip().lower() if color else None
        for slot_num, (reg_num, col) in self.parking_lot.occupied_slots.items():
            if color == col: yield slot_num

    def registration_numbers_by_color(self, color):
        """
        Yields the `registration_number`, if the vehicle occupying the slot has a specific color.

        :param color:
        """
        color = color.strip().lower() if color else None
        for slot_num, (reg_num, col) in self.parking_lot.occupied_slots.items():
            if color == col: yield reg_num

    # Time complexity: O(1)
    def slot_number_by_registration_number(self, registration_number):
        """
        Looks up the `registration_number`, and returns the `slot_number`.

        :param registration_number:
        """
        return self.parking_lot.get_slot_by_reg_num(registration_number)