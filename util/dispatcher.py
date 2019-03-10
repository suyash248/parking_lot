__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from util.parser import parse
from services.parking import ParkingService
from util.constants import Command, ErrorConstant, Response
from util.logger import logger
from models.vehicle import Vehicle, Car
from models.slot import SmallSlot

class Dispatcher(object):
    """
    Executes the command(@see `util.constants.Command`) and subsequently takes the appropriate action(s).
    """

    parking_service: ParkingService = ParkingService()

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
            if cmd_key != Command.CREATE and self.parking_service.parking_lot is None:
                logger.error("No parking lot found, please create a parking lot first.")
                response = Response(success=False, error=ErrorConstant.NO_PARKING_LOT_FOUND,
                                    message="Parking lot must be created first")
                return response

            if cmd_key == Command.CREATE:
                size = int(parsed_cmd.get('size', 0))
                self.parking_service.create_parking_lot(size)
                logger.info("Created a parking lot with {} slots".format(size))
                response = Response(data={'size': size}, message="Parking lot created successfully.")

            elif cmd_key == Command.PARK:
                reg_num = parsed_cmd.get('reg_num')
                color = parsed_cmd.get('color')

                # Create vehicle.
                vehicle = Vehicle.create(Car, reg_num, color)

                # Park the vehicle.
                response = self.parking_service.park(vehicle)
                if response.success:
                    logger.info("Allocated slot number: {}".format(response.data['slot_num']))
                else:
                    if response.error == ErrorConstant.PARKING_LOT_OVERFLOW:
                        logger.info("Sorry, parking lot is full")

            elif cmd_key == Command.LEAVE:
                slot_num = int(parsed_cmd.get('slot_num'))

                # Vehicle is leaving the slot.
                response = self.parking_service.leave(SmallSlot(int(slot_num)))
                if response.success:
                    logger.info("Slot number {} is free".format(slot_num))

            elif cmd_key == Command.STATUS:
                logger.info("Slot No.\tRegistration No.\tColour")
                for slot_num, reg_num, col in self.parking_service.status():
                    logger.info('{}\t\t\t{}\t\t{}'.format(slot_num, reg_num, col))

            elif cmd_key == Command.REG_NUMS_BY_COLOR:
                color = parsed_cmd.get('color')

                # Will be better to print reg_num one-by-one, as it will save the space.
                reg_nums = [reg_num for reg_num in self.parking_service.registration_numbers_by_color(color)]
                logger.info(', '.join(reg_nums))
                response = Response(data={'reg_nums': reg_nums})

            elif cmd_key == Command.SLOT_NUMS_BY_COLOR:
                color = parsed_cmd.get('color')

                # Will be better to print slot_num one-by-one, as it will save the space.
                slot_nums = [str(slot_num) for slot_num in self.parking_service.slot_numbers_by_color(color)]
                logger.info(', '.join(slot_nums))
                response = Response(data={'slot_nums': slot_nums})

            elif cmd_key == Command.SLOT_NUM_BY_REG_NUM:
                reg_num = parsed_cmd.get('reg_num')
                slot_num = self.parking_service.slot_number_by_registration_number(reg_num)
                logger.info(str(slot_num or 'Not found'))
                response = Response(success=slot_num is not None, data={'slot_num': slot_num})

            else:
                logger.error("Invalid command: {}".format(cmd))
                response = Response(success=False, error=ErrorConstant.INVALID_COMMAND)

        else:
            logger.error("Invalid command: {}".format(cmd))
            response = Response(success=False, error=ErrorConstant.INVALID_COMMAND)

        return response
