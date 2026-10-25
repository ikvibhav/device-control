import random
from src.vector import Vector2D
from src.utils import MARK_MEASUREMENT_OFFSET, TWOD_MEASUREMENT_OFFSET

class MeasuringDevice:
    """MeasuringDevice represents performing 2D measurements and mark measurements."""

    # Nominal offset from PU centre to MD
    NOMINAL_OFFSET = Vector2D(100, 10)

    def __init__(self):
        """
        Initialize the measuring device with a default calibration offset.
        """
        self.calibration_offset = Vector2D(0.0, 0.0)

    def set_calibration_offset(self, offset: Vector2D):
        """
        Set the calibration offset for the measuring device.
        """
        self.calibration_offset = offset

    def get_calibration_offset(self) -> Vector2D:
        """
        Get the current calibration offset of the measuring device.
        """
        return self.calibration_offset

    def get_actual_position(self, pu_centre: Vector2D) -> Vector2D:
        """
        Get the actual position of the measuring device based on the PU centre.
        """
        return pu_centre + self.NOMINAL_OFFSET + self.calibration_offset

    def measure_2d(self) -> Vector2D:
        """
        Perform 2D measurement at current location
        The scan area is 50x50 um.
        """
        offset_x = random.uniform(-TWOD_MEASUREMENT_OFFSET, TWOD_MEASUREMENT_OFFSET)
        offset_y = random.uniform(-TWOD_MEASUREMENT_OFFSET, TWOD_MEASUREMENT_OFFSET)
        return self.NOMINAL_OFFSET + self.calibration_offset + Vector2D(offset_x, offset_y)

    def measure_mark(self) -> Vector2D:
        """
        Perform mark measurement at current location.
        The scan area is 50x50 um.
        """
        offset_x = random.uniform(-MARK_MEASUREMENT_OFFSET, MARK_MEASUREMENT_OFFSET)
        offset_y = random.uniform(-MARK_MEASUREMENT_OFFSET, MARK_MEASUREMENT_OFFSET)
        return self.NOMINAL_OFFSET + self.calibration_offset + Vector2D(offset_x, offset_y)
    