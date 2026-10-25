import math
from src.vector import Vector2D


class Wafer:
    """
    Represents a wafer with -
    1. Shot representing the grid layout of the wafer
    2. Mark representing the bottom right corner of each grid
    """

    # Wafer dimensions
    MARK_WIDTH = 40
    MARK_HEIGHT = 30
    SHOT_WIDTH = 200
    SHOT_HEIGHT = 400

    # Center mark position in WAFER_CS (relative to wafer center)
    CENTER_MARK_WAFER_CS = Vector2D(10, 30)
    
    # Nominal wafer center in PU_CS
    NOMINAL_CENTER_PU_CS = Vector2D(200_000, 300_000)
    
    # Maximum placement error
    MAX_PLACEMENT_ERROR = 50  # micrometers in x and y
    MAX_ROTATION_ERROR = 2    # degrees

    def __init__(self):
        """Initialize the wafer object"""
        self.center_pu_cs = Vector2D(self.NOMINAL_CENTER_PU_CS.x_um, self.NOMINAL_CENTER_PU_CS.y_um)
        self.placement_error = Vector2D(0, 0)
        self.rotation_error = 0

    def get_shot_position(self, shot_x: int, shot_y: int) -> Vector2D:
        """
        Get the center position of a shot in WAFER_CS
        Shots are indexed from center (0,0)

        Args:
            shot_x (int): The x-index of the shot relative to the wafer center.
            shot_y (int): The y-index of the shot relative to the wafer center.

        Returns:
            Vector2D: The center position of the shot in WAFER_CS.
        """
        x = shot_x * self.SHOT_WIDTH + self.SHOT_WIDTH / 2
        y = shot_y * self.SHOT_HEIGHT + self.SHOT_HEIGHT / 2
        return Vector2D(x, y)

    def get_mark_position(self, mark_x: int, mark_y: int) -> Vector2D:
        """
        Get the bottom right corner position of a shot (mark) in WAFER_CS
        Marks are indexed from center (0,0)
        Mark is at bottom-right corner of each shot.

        Args:
            mark_x (int): The x-index of the mark relative to the wafer center.
            mark_y (int): The y-index of the mark relative to the wafer center.

        Returns:
            Vector2D: The bottom right corner position of the mark in WAFER_CS.
        """
        shot_center = self.get_shot_position(mark_x, mark_y)

        mark_offset_x = self.SHOT_WIDTH / 2 - self.MARK_WIDTH / 2
        mark_offset_y = self.SHOT_HEIGHT / 2 - self.MARK_HEIGHT / 2

        return shot_center + Vector2D(mark_offset_x, mark_offset_y)

    def rotate_point(self, point: Vector2D, angle_degrees: float) -> Vector2D:
        """
        Rotate a point around the origin by a given angle.

        Args:
            point (Vector2D): The point to rotate.
            angle_degrees (float): The rotation angle in degrees.

        Returns:
            Vector2D: The rotated point.
        """
        # 1. Extract the rotation angle in radians
        angle_radians = math.radians(angle_degrees)

        # 2. Compute the cosine and sine of the rotation angle
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)

        # 3. Apply the rotation matrix to the point
        # Follows the standard 2D rotation matrix formula: [x'] = [cos -sin][x]
        #                                           [y']   [sin  cos][y]
        x_new = point.x_um * cos_theta - point.y_um * sin_theta
        y_new = point.x_um * sin_theta + point.y_um * cos_theta
        return Vector2D(x_new, y_new)

    def wafer_cs_to_pu_cs(self, point_wafer_cs: Vector2D) -> Vector2D:
        """
        Convert a point from WAFER_CS to PU_CS 
        Accounts for:
        1. Wafer Rotation
        2. Wafer Placement (Center Offset)
        3. Wafer Placement Error (Translation and Rotation)

        Args:
            point_wafer_cs (Vector2D): The point in WAFER_CS to convert.

        Returns:
            Vector2D: The corresponding point in PU_CS.
        """

        # 1. Apply wafer rotation error
        rotated = self.rotate_point(point_wafer_cs, self.rotation_error)

        # 2. Apply wafer placement (center offset)
        result = self.center_pu_cs + rotated + self.placement_error

        return result