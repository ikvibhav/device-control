from src.vector import Vector2D


class CalibrationStation:
    """
    Represents a calibration station that can be used to calibrate devices.
    """

    # Location of calibration station in PU_CS
    LOCATION = Vector2D(1500, 300_000)

    def __init__(self):
        """ Initializes the calibration station. """
        pass

    @staticmethod
    def get_location():
        """ Returns the location of the calibration station. """
        return CalibrationStation.LOCATION