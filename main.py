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

    # Part 2, Step 2: Get wafer position and rotation
    rotation, centre_pu_cs = controller.get_wafer_position_and_rotation()
    print(f"Wafer Rotation: {rotation}")
    print(f"Wafer Centre PU_CS: {centre_pu_cs}")

    # Part 2, Step 3: Measure the centre mark
    centre_mark_pu_cs = controller.measure_center_mark()
    print(f"Centre Mark PU_CS: {centre_mark_pu_cs}")

    # Part 2, Step 4: Measure the offset mark (2 shots up, 1 shot right)
    offset_mark_pu_cs = controller.measure_offset_mark()
    print(f"Offset Mark PU_CS: {offset_mark_pu_cs}")