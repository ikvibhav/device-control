import unittest
from unittest.mock import patch

from src.measuring_device import MeasuringDevice
from src.vector import Vector2D


class TestMeasuringDevice(unittest.TestCase):
    def test_set_and_get_calibration_offset(self):
        device = MeasuringDevice()
        offset = Vector2D(4.0, -3.0)

        device.set_calibration_offset(offset)

        self.assertIs(device.get_calibration_offset(), offset)

    def test_get_actual_position_adds_nominal_and_calibration_offsets(self):
        device = MeasuringDevice()
        device.set_calibration_offset(Vector2D(2.0, -4.0))
        pu_centre = Vector2D(1000.0, 2000.0)

        actual = device.get_actual_position(pu_centre)

        self.assertEqual(actual.x_um, 1102.0)
        self.assertEqual(actual.y_um, 2006.0)

    @patch("src.measuring_device.random.uniform", side_effect=[25.0, -25.0, 50.0, -50.0])
    def test_measure_methods_apply_random_offsets_within_configured_ranges(self, _):
        device = MeasuringDevice()
        device.set_calibration_offset(Vector2D(1.0, 2.0))

        measured_2d = device.measure_2d()
        measured_mark = device.measure_mark()

        self.assertEqual(measured_2d.x_um, 126.0)
        self.assertEqual(measured_2d.y_um, -13.0)
        self.assertEqual(measured_mark.x_um, 151.0)
        self.assertEqual(measured_mark.y_um, -38.0)
