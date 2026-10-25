import math
from src.vector import Vector2D
from src.positioning_unit import PositioningUnit
from src.wafer import Wafer
from src.calibration_station import CalibrationStation


class DeviceController:
    """
    Main Controller that orchestrates device operations 
    involving the Positioning Unit, Wafer, and Calibration Station.
    """

    def __init__(self, positioning_unit: PositioningUnit, wafer: Wafer, calibration_station: CalibrationStation):
        self.positioning_unit = positioning_unit
        self.wafer = wafer
        self.calibration_station = calibration_station
        self.calibration_offset = None

    def perform_calibration(self) -> Vector2D:
        """
        Part 2, Step 1: Perform calibration measurement.
        
        Determine the offset vector between PU center and MD 
        at the calibration station.
        """

        # 1. Move PU to the calibration station
        calibration_position = self.calibration_station.get_location()
        self.positioning_unit.move_pu(calibration_position.x_um, calibration_position.y_um)

        # 2. Perform calibration measurement (Returns a random offset vector)
        self.calibration_offset = self.positioning_unit.measuring_device.calibration_measurement()

        # 3. Set the calibration offset for future measurements
        self.positioning_unit.measuring_device.set_calibration_offset(self.calibration_offset)

        # 4. Return the calibration offset for reference
        return self.calibration_offset