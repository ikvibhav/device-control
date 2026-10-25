from src.vector import Vector2D
from src.measuring_device import MeasuringDevice

class PositioningUnit:
    def __init__(self):
        self.current_position = Vector2D(0.0, 0.0)
        self.measuring_device = MeasuringDevice()

    def move_pu(self, target_x_um: float, target_y_um: float):
        self.current_position = Vector2D(target_x_um, target_y_um)

    def get_pu_position(self) -> Vector2D:
        return self.current_position

    def get_md_position(self) -> Vector2D:
        return self.measuring_device.get_actual_position(self.current_position)