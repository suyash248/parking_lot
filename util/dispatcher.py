__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from util.parser import parse
from services.parking_lot import ParkingLotService
from util.constants import Command, ErrorConstant, Response
from util.logger import logger
from models.vehicle import Vehicle, Car
from models.slot import Slot, SmallSlot

class Dispatcher(object):
    """
    Executes the command(@see `util.constants.Command`) and subsequently takes the appropriate action(s).
    """
    def __init__(self):
        pass

    def dispatch(self, cmd):
        """
        Executes the command.
        :param cmd: command to be executed.
        """
        response = Response()
        cmd_key, parsed_cmd = parse(cmd)
        if cmd_key and parsed_cmd:
            pass

        return response
