from src.wafer import Wafer, Vector2D

class TestWafer:

    def test_get_shot_position(self):
        wafer = Wafer()
        shot_position = wafer.get_shot_position(1, 2)
        assert isinstance(shot_position, Vector2D)

    def test_get_mark_position(self):
        wafer = Wafer()
        mark_position = wafer.get_mark_position(1, 2)
        assert isinstance(mark_position, Vector2D)

    def test_rotate_point_90_degrees(self):
        wafer = Wafer()
        point = Vector2D(1, 0)
        rotated_point = wafer.rotate_point(point, 90)
        assert isinstance(rotated_point, Vector2D)

    def test_rotate_point_180_degrees(self):
        wafer = Wafer()
        point = Vector2D(1, 0)
        rotated_point = wafer.rotate_point(point, 180)
        assert isinstance(rotated_point, Vector2D)

    def test_wafer_cs_to_pu_cs_without_rotation_error(self):
        wafer = Wafer()
        point_wafer_cs = Vector2D(100, 200)
        point_pu_cs = wafer.wafer_cs_to_pu_cs(point_wafer_cs)
        assert isinstance(point_pu_cs, Vector2D)
        assert point_pu_cs.x_um == wafer.center_pu_cs.x_um + point_wafer_cs.x_um
        assert point_pu_cs.y_um == wafer.center_pu_cs.y_um + point_wafer_cs.y_um

    def test_wafer_cs_to_pu_cs_with_rotation_error(self):
        wafer = Wafer()
        wafer.rotation_error = 90
        point_wafer_cs = Vector2D(100, 0)
        point_pu_cs = wafer.wafer_cs_to_pu_cs(point_wafer_cs)
        assert isinstance(point_pu_cs, Vector2D)
        # After 90 degree rotation, (100,0) becomes (0,100)
        assert point_pu_cs.x_um == wafer.center_pu_cs.x_um + 0
        assert point_pu_cs.y_um == wafer.center_pu_cs.y_um + 100