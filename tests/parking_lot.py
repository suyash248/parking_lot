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

    def test_3_create(self):
        size = 7
        response = self.create_parking_lot(size=size)
        self.assertEqual(size, int(response.data.get('size', 0)))

    def test_4_park(self):
        c_response = self.create_parking_lot(size=5)
        self.assertTrue(c_response.success)

        for i in range(0, 7):
            # PARKING_LOT_OVERFLOW
            p_response = self.dispatcher.dispatch("park DL-3C-909{} GREY".format(i))
            if not p_response.success:
                self.assertIn(p_response.error, (ErrorConstant.PARKING_LOT_OVERFLOW,
                                                 ErrorConstant.NO_PARKING_LOT_FOUND,
                                                 ErrorConstant.SLOT_OCCUPIED,
                                                 ErrorConstant.VEHICLE_IS_ALREADY_PARKED))

        c_response = self.create_parking_lot(size=5)
        self.assertTrue(c_response.success)
        for i in range(0, 5):
            # VEHICLE_IS_ALREADY_PARKED
            p_response = self.dispatcher.dispatch("park DL-3C-9010 GREY")
            if not p_response.success:
                self.assertIn(p_response.error, (ErrorConstant.PARKING_LOT_OVERFLOW,
                                             ErrorConstant.NO_PARKING_LOT_FOUND,
                                             ErrorConstant.SLOT_OCCUPIED,
                                             ErrorConstant.VEHICLE_IS_ALREADY_PARKED))

    def test_5_leave(self):
        c_response = self.create_parking_lot(size=5)
        self.assertTrue(c_response.success)

        reg_nums = ["DL-3C-9070", "DL-3C-9071"]
        for reg_num in reg_nums:
            self.dispatcher.dispatch("park {} GREY".format(reg_num))

        for slot_num in range(1, 7):
            l_res = self.dispatcher.dispatch("leave {}".format(slot_num))
            if not l_res.success:
                self.assertEqual(l_res.error, ErrorConstant.INVALID_SLOT, msg="Invalid slot")
            else:
                reg_num = l_res.data.get('reg_num', None)
                self.assertEqual(reg_num, reg_nums[slot_num-1])


    def create_parking_lot(self, size=5):
        cmd = "create_parking_lot {}".format(str(size))
        response = self.dispatcher.dispatch(cmd)
        return response

if __name__ == '__main__':
    unittest.main()
    # python -m unittest discover -s 'tests' -p '*.py'