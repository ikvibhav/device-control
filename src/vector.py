import math


class Vector2D:
    """Represents a 2D vector with x and y components in micrometers."""

    def __init__(self, x_um: float, y_um: float):
        self.x_um = x_um
        self.y_um = y_um

    def __add__(self, other: "Vector2D") -> "Vector2D":
        """Adds two Vector2D objects component-wise."""
        return Vector2D(self.x_um + other.x_um, self.y_um + other.y_um)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        """Subtracts two Vector2D objects component-wise."""
        return Vector2D(self.x_um - other.x_um, self.y_um - other.y_um)

    def magnitude(self) -> float:
        """Returns the magnitude of the vector."""
        return math.sqrt(self.x_um ** 2 + self.y_um ** 2)

    def angle_degrees(self) -> float:
        """Returns the angle of the vector in degrees relative to the positive x-axis."""
        return math.degrees(math.atan2(self.y_um, self.x_um))

    def __repr__(self) -> str:
        """Returns a string representation of the vector."""
        return f"Vector2D(x_um={self.x_um}, y_um={self.y_um})"