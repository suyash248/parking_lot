__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from abc import ABC
from util.contants import VehicleSize

class Vehicle(ABC):
    """
    Base class of all the vehicle types.
    """
    num_wheels = -1
    size = VehicleSize.SMALL

    def __init__(self, registration_number, color, *args, **kwargs):
        self.registration_number = registration_number
        self.color = color.lower() if color else ''

    @staticmethod
    def create(kind, registration_number, color, *args, **kwargs):
        vehicle = None
        if issubclass(kind, (Vehicle, )):
            vehicle = kind(registration_number, color, *args, **kwargs)
        return vehicle

class Car(Vehicle):
    """
    Represents a car.
    """
    num_wheels = 4