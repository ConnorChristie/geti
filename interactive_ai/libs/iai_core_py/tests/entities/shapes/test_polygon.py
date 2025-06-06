# Copyright (C) 2022-2025 Intel Corporation
# LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE


import pytest

from iai_core.entities.shapes import Point, Polygon, Rectangle
from iai_core.utils.time_utils import now


class TestPoint:
    def coordinates(self):
        return [0.5, 0.4]

    def point(self):
        return Point(*self.coordinates())

    def test_point_normalize_wrt_roi(self):
        """
        <b>Description:</b>
        Check Point normalize_wrt_roi methods

        <b>Input data:</b>
        Initialized instance of Point
        Initialized instance of Rectangle

        <b>Expected results:</b>
        Test passes if Point normalize_wrt_roi returns correct values

        <b>Steps</b>
        1. Initialize Point instance
        2. Check returning value
        """

        point = self.point()
        roi = Rectangle(x1=0.3, x2=0.5, y1=0.3, y2=0.5)
        normalized = point.normalize_wrt_roi(roi)
        assert normalized.x == 0.4
        assert normalized.y == 0.38

    def test_point_denormalize_wrt_roi_shape(self):
        """
        <b>Description:</b>
        Check Point denormalize_wrt_roi_shape methods

        <b>Input data:</b>
        Initialized instance of Point
        Initialized instance of Rectangle

        <b>Expected results:</b>
        Test passes if Point denormalize_wrt_roi_shape returns correct values

        <b>Steps</b>
        1. Initialize Point instance
        2. Check returning value
        """

        point = self.point()
        roi = Rectangle(x1=0.4, x2=0.5, y1=0.3, y2=0.5)
        normalized = point.denormalize_wrt_roi_shape(roi)
        assert normalized.x == 1.0
        assert normalized.y == 0.5000000000000001


class TestPolygon:
    modification_date = now()

    def points(self):
        point1 = Point(0.5, 0.0)
        point2 = Point(0.75, 0.2)
        point3 = Point(0.6, 0.1)
        return [point1, point2, point3]

    def other_points(self):
        point1 = Point(0.3, 0.1)
        point2 = Point(0.8, 0.3)
        point3 = Point(0.6, 0.2)
        return [point1, point2, point3]

    def polygon(self):
        return Polygon(self.points(), modification_date=self.modification_date)

    def other_polygon(self):
        return Polygon(self.other_points(), modification_date=self.modification_date)

    def test_polygon(self):
        """
        <b>Description:</b>
        Check Polygon parameters

        <b>Input data:</b>
        Points

        <b>Expected results:</b>
        Test passes if Polygon correctly calculates parameters and returns default values

        <b>Steps</b>
        1. Check Polygon params
        2. Check Polygon default values
        3. Check Polygon with empty points
        """

        polygon = self.polygon()
        modification_date = self.modification_date
        assert len(polygon.points) == 3
        assert polygon.modification_date == modification_date
        assert polygon.points == self.points()

        empty_points_list = []
        with pytest.raises(ValueError):
            Polygon(empty_points_list)

    def test_polygon_normalize_wrt_roi_shape(self):
        """
        <b>Description:</b>
        Check Polygon normalize_wrt_roi_shape methods

        <b>Input data:</b>
        Initialized instance of Polygon
        Initialized instance of Rectangle

        <b>Expected results:</b>
        Test passes if Polygon normalize_wrt_roi_shape returns correct values

        <b>Steps</b>
        1. Initialize Polygon instance
        2. Check returning value
        """

        polygon = self.polygon()
        roi = Rectangle(x1=0.0, x2=0.5, y1=0.0, y2=0.5)
        normalized = polygon.normalize_wrt_roi_shape(roi)
        assert len(normalized.points) == 3
        assert normalized.min_x == 0.25
        assert normalized.max_x == 0.375
        assert normalized.min_y == 0.0
        assert normalized.max_y == 0.1

        with pytest.raises(ValueError):
            polygon.normalize_wrt_roi_shape("123")

    def test_polygon_denormalize_wrt_roi_shape(self):
        """
        <b>Description:</b>
        Check Polygon denormalize_wrt_roi_shape methods

        <b>Input data:</b>
        Initialized instance of Polygon
        Initialized instance of Rectangle

        <b>Expected results:</b>
        Test passes if Polygon denormalize_wrt_roi_shape returns correct values

        <b>Steps</b>
        1. Initialize Polygon instance
        2. Check returning value
        """

        polygon = self.polygon()
        roi = Rectangle(x1=0.5, x2=1.0, y1=0.0, y2=1.0)
        denormalized = polygon.denormalize_wrt_roi_shape(roi)
        assert len(denormalized.points) == 3
        assert denormalized.min_x == 0.0
        assert denormalized.max_x == 0.5
        assert denormalized.min_y == 0.0
        assert denormalized.max_y == 0.2

        with pytest.raises(ValueError):
            polygon.denormalize_wrt_roi_shape("123")

    def test_polygon__as_shapely_polygon(self):
        """
        <b>Description:</b>
        Check Polygon _as_shapely_polygon methods

        <b>Input data:</b>
        Initialized instance of Polygon

        <b>Expected results:</b>
        Test passes if Polygon _as_shapely_polygon returns correct values

        <b>Steps</b>
        1. Initialize Polygon instance
        2. Check returning value
        """

        polygon = self.polygon()
        polygon2 = self.other_polygon()
        shapely_polygon = polygon._as_shapely_polygon()
        shapely_polygon2 = polygon2._as_shapely_polygon()
        assert shapely_polygon.area == 0.0025000000000000022
        assert str(shapely_polygon) == "POLYGON ((0.5 0, 0.75 0.2, 0.6 0.1, 0.5 0))"
        assert shapely_polygon != shapely_polygon2

    def test_polygon_get_area(self):
        """
        <b>Description:</b>
        Check Polygon get_area method

        <b>Input data:</b>
        Initialized instance of Polygon

        <b>Expected results:</b>
        Test passes if Polygon get_area returns correct values

        <b>Steps</b>
        1. Initialize Polygon instance
        2. Check returning value
        """

        polygon = self.polygon()
        polygon2 = self.other_polygon()
        area = polygon.get_area()
        area2 = polygon2.get_area()
        assert area == 0.0025000000000000022
        assert area != area2
