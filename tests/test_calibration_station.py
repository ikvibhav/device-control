import unittest
from src.calibration_station import CalibrationStation


class TestCalibrationStation(unittest.TestCase):
    def test_get_location(self):
        location = CalibrationStation.get_location()
        self.assertEqual(location.x_um, 1500)
        self.assertEqual(location.y_um, 300_000)