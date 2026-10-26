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
        
        # To be determined during execution
        self.calibration_offset = None
        self.estimated_rotation_deg = 0.0
        self.estimated_center_pu_cs = Vector2D(
            Wafer.NOMINAL_CENTER_PU_CS.x_um,
            Wafer.NOMINAL_CENTER_PU_CS.y_um,
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _mark_wafer_cs(shots_right: int, shots_up: int) -> Vector2D:
        """WAFER_CS position of a mark, offset from the centre mark by whole shots."""
        centre = Wafer.CENTER_MARK_WAFER_CS
        return Vector2D(
            centre.x_um + shots_right * Wafer.SHOT_WIDTH,
            centre.y_um + shots_up * Wafer.SHOT_HEIGHT,
        )

    def _md_offset_from_pu_centre(self) -> Vector2D:
        """Offset from PU centre to MD: nominal plus calibration, from MeasuringDevice."""
        return self.positioning_unit.measuring_device.get_actual_position(Vector2D(0.0, 0.0))

    def move_md_to(self, target_pu_cs: Vector2D) -> None:
        """Move the PU so that the measuring device is over target_pu_cs."""
        pu_target = target_pu_cs - self._md_offset_from_pu_centre()
        self.positioning_unit.move_pu(pu_target.x_um, pu_target.y_um)

    def _find_mark(self, expected_pu_cs: Vector2D) -> Vector2D:
        """Move the MD to the expected mark position and return where the mark was found."""
        self.move_md_to(expected_pu_cs)
        offset = self.positioning_unit.measuring_device.measure_mark()
        return expected_pu_cs + offset

    def wafer_to_pu_cs(self, point_wafer_cs: Vector2D) -> Vector2D:
        """Map a WAFER_CS point to PU_CS using the controller's estimates."""
        rotated = self.wafer.rotate_point(point_wafer_cs, self.estimated_rotation_deg)
        return self.estimated_center_pu_cs + rotated

    # ------------------------------------------------------------------
    # Executions
    # ------------------------------------------------------------------

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

    def get_wafer_position_and_rotation(self) -> tuple[float, Vector2D]:
        """
        Part 2, Step 2: Find 
        1. The wafer rotation and centre from centre mark
        2. The mark two shots to the left
        """

        # 1. Get the wafer positions
        centre_wafer = self._mark_wafer_cs(0, 0)
        left_wafer = self._mark_wafer_cs(-2, 0)

        # 2. Expected positions in PU_CS
        # Assuming no wafer rotation for expected positions
        centre_expected = Wafer.NOMINAL_CENTER_PU_CS + centre_wafer
        left_expected = Wafer.NOMINAL_CENTER_PU_CS + left_wafer

        # 3. Find the actual positions using the measuring device
        centre_actual = self._find_mark(centre_expected)
        left_actual = self._find_mark(left_expected)

        # 4. Compute Rotation
        measured_baseline = centre_actual - left_actual
        expected_baseline = centre_expected - left_expected
        rotation = math.atan2(measured_baseline.y_um, measured_baseline.x_um) - math.atan2(expected_baseline.y_um, expected_baseline.x_um)

        # 5. Centre
        centre_pu_cs = centre_actual - self.wafer.rotate_point(centre_wafer, math.degrees(rotation))

        self.estimated_rotation_deg = math.degrees(rotation)
        self.estimated_center_pu_cs = centre_pu_cs

        return rotation, centre_pu_cs

    def measure_center_mark(self) -> Vector2D:
        """
        Part 2, Step 3:
        1. Move MD to middle of centre mark on the wafer
        2. Perform the 2D measurement using the measuring device.
        """
        target_pu_cs = self.wafer_to_pu_cs(self._mark_wafer_cs(0, 0))
        self.move_md_to(target_pu_cs)
        return self.positioning_unit.measuring_device.measure_2d()

    def measure_offset_mark(self) -> Vector2D:
        """
        Part 2, Step 4:
        1. Move MD to the offset mark on the wafer (2 shots up, 1 shot right)
        2. Perform the 2D measurement using the measuring device.
        """
        target_pu_cs = self.wafer_to_pu_cs(self._mark_wafer_cs(1, 2))
        self.move_md_to(target_pu_cs)
        return self.positioning_unit.measuring_device.measure_2d()
        