__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import unittest
from util.constants import ErrorConstant
from util.dispatcher import Dispatcher
from util.parser import parse
from uuid import uuid4

class TestParkingLot(unittest.TestCase):

    def setUp(self):
        self.dispatcher = Dispatcher()

    def tearDown(self):
        self.dispatcher = None

    def test_1_parse_cmd(self):
        cmd = "CMD_{}".format(str(uuid4()))
        cmd_key, parsed_data = parse(cmd)
        self.assertIsNone(cmd_key, msg="{} is invalid command, command key must be null".format(cmd))
        self.assertIsNone(parsed_data, msg="{} is invalid command, command info must be null".format(cmd))

        cmd = "status"
        cmd_key, parsed_data = parse(cmd)
        self.assertIsNotNone(cmd_key, msg="{} is valid command, command key must not be null".format(cmd))
        self.assertIsNotNone(parsed_data, msg="{} is valid command, command info must not be null".format(cmd))

    def test_2_check_if_parking_lot_available(self):
        cmd = "status"
        response = self.dispatcher.dispatch(cmd)
        if not response.success:
            self.assertEqual(response.error, ErrorConstant.NO_PARKING_LOT_FOUND)



    def create_parking_lot(self, size=5):
        cmd = "create_parking_lot {}".format(str(size))
        response = self.dispatcher.dispatch(cmd)
        return response

if __name__ == '__main__':
    unittest.main()
    # python -m unittest discover -s 'tests' -p '*.py'