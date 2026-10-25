import unittest

from src.vector import Vector2D


class TestVector2D(unittest.TestCase):
    def test_add_returns_component_wise_sum(self):
        left = Vector2D(10.5, -2.0)
        right = Vector2D(1.5, 5.0)

        result = left + right

        self.assertEqual(result.x_um, 12.0)
        self.assertEqual(result.y_um, 3.0)

    def test_subtract_returns_component_wise_difference(self):
        left = Vector2D(10.5, -2.0)
        right = Vector2D(1.5, 5.0)

        result = left - right

        self.assertEqual(result.x_um, 9.0)
        self.assertEqual(result.y_um, -7.0)

    def test_magnitude_uses_pythagorean_distance(self):
        vector = Vector2D(3.0, 4.0)

        self.assertEqual(vector.magnitude(), 5.0)

    def test_angle_degrees_returns_expected_cardinal_angles(self):
        self.assertEqual(Vector2D(0.0, 1.0).angle_degrees(), 90.0)
        self.assertEqual(Vector2D(-1.0, 0.0).angle_degrees(), 180.0)

    def test_repr_contains_coordinates(self):
        vector = Vector2D(1.25, -3.5)

        self.assertEqual(repr(vector), "Vector2D(x_um=1.25, y_um=-3.5)")