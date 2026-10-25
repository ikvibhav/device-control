import unittest

from src.positioning_unit import PositioningUnit
from src.vector import Vector2D


class TestPositioningUnit(unittest.TestCase):
    def test_move_pu_updates_current_position(self):
        unit = PositioningUnit()

        unit.move_pu(12.5, -8.0)

        current = unit.get_pu_position()
        self.assertEqual(current.x_um, 12.5)
        self.assertEqual(current.y_um, -8.0)

    def test_get_md_position_reflects_pu_position_and_calibration(self):
        unit = PositioningUnit()
        unit.move_pu(300.0, 400.0)
        unit.measuring_device.set_calibration_offset(Vector2D(3.0, 4.0))

        measured_device_position = unit.get_md_position()

        self.assertEqual(measured_device_position.x_um, 403.0)
        self.assertEqual(measured_device_position.y_um, 414.0)
