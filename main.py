from src.device_controller import DeviceController
from src.positioning_unit import PositioningUnit
from src.wafer import Wafer
from src.calibration_station import CalibrationStation


if __name__ == "__main__":
    positioning_unit = PositioningUnit()
    wafer = Wafer()
    calibration_station = CalibrationStation()

    controller = DeviceController(positioning_unit, wafer, calibration_station)

    # Part 2, Step 1: Perform calibration
    calibration_offset = controller.perform_calibration()
    print(f"Calibration Offset: {calibration_offset}")
