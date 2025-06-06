# Copyright (C) 2022-2025 Intel Corporation
# LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

import itertools
import warnings

import pytest

from iai_core.entities.shapes import Ellipse, Point, Polygon, Rectangle, Shape


class TestShape:
    @staticmethod
    def fully_covering_rectangle() -> Rectangle:
        return Rectangle.generate_full_box()

    @staticmethod
    def fully_covering_ellipse() -> Ellipse:
        return Ellipse(x1=0.0, y1=0.0, x2=1.0, y2=1.0)

    @staticmethod
    def fully_covering_polygon() -> Polygon:
        return Polygon(
            [
                Point(0.0, 0.1),
                Point(0.0, 0.9),
                Point(0.5, 1.0),
                Point(1.0, 0.9),
                Point(1.0, 0.0),
                Point(0.0, 0.1),
            ]
        )

    def rectangle(self) -> Rectangle:
        return Rectangle(x1=0.2, y1=0.2, x2=0.6, y2=0.7)

    def ellipse(self) -> Ellipse:
        return Ellipse(x1=0.4, y1=0.1, x2=0.9, y2=0.8)

    def polygon(self) -> Polygon:
        return Polygon(
            [
                Point(0.3, 0.4),
                Point(0.3, 0.7),
                Point(0.5, 0.75),
                Point(0.8, 0.7),
                Point(0.8, 0.4),
                Point(0.3, 0.4),
            ],
        )

    @staticmethod
    def not_inscribed_rectangle() -> Rectangle:
        return Rectangle(x1=0.0, y1=0.0, x2=0.01, y2=0.01)

    @staticmethod
    def not_inscribed_ellipse() -> Ellipse:
        return Ellipse(x1=0.0, y1=0.0, x2=0.01, y2=0.01)

    @staticmethod
    def not_inscribed_polygon() -> Polygon:
        return Polygon(
            [
                Point(0.0, 0.0),
                Point(0.0, 0.01),
                Point(0.01, 0.02),
                Point(0.02, 0.01),
                Point(0.02, 0.0),
                Point(0.0, 0.0),
            ]
        )

    @staticmethod
    def lower_side_intersect_shapes() -> list:
        return [
            Rectangle(x1=0.2, y1=0.1, x2=0.5, y2=0.4),
            Polygon(
                [
                    Point(0.35, 0.1),
                    Point(0.2, 0.2),
                    Point(0.2, 0.4),
                    Point(0.5, 0.4),
                    Point(0.5, 0.2),
                    Point(0.35, 0.1),
                ]
            ),
        ]

    @staticmethod
    def upper_side_intersect_shapes() -> list:
        return [
            Rectangle(x1=0.2, y1=0.4, x2=0.5, y2=0.7),
            Polygon(
                [
                    Point(0.35, 0.7),
                    Point(0.2, 0.6),
                    Point(0.2, 0.4),
                    Point(0.5, 0.4),
                    Point(0.5, 0.6),
                    Point(0.35, 0.7),
                ]
            ),
        ]

    def test_shape_get_area_method(self):
        """
        <b>Description:</b>
        Check get_area not implemented method of Shape class

        <b>Expected results:</b>
        Test passes if NotImplementedError exception raised when using get_area method on Shape instance
        """
        for shape in [self.rectangle(), self.ellipse(), self.polygon()]:
            with pytest.raises(NotImplementedError):
                Shape.get_area(shape)

    def test_shape_intersects(self):
        """
        <b>Description:</b>
        Check Shape intersects method for Rectangle, Ellipse and Polygon objects

        <b>Expected results:</b>
        Test passes if intersects method returns expected values

        <b>Steps</b>
        1. Check intersects method when Shapes intersect completely
        2. Check intersects method when Shapes intersect in several points
        3. Check intersects method when Shapes intersect by one side
        4. Check intersects method when Shapes not intersect
        5. Check GeometryException exception raised with incorrect parameters for intersect method
        """
        inscribed_shapes_list = [self.rectangle(), self.ellipse(), self.polygon()]
        # Check when Shapes intersect fully
        for full_element in [
            self.fully_covering_rectangle(),
            self.fully_covering_ellipse(),
            self.fully_covering_polygon(),
        ]:
            for inscribed in inscribed_shapes_list:
                assert full_element.intersects(inscribed)
                assert inscribed.intersects(full_element)
        # Check when Shapes intersect in several points
        for shape, other_shape in list(itertools.combinations(inscribed_shapes_list, 2)):
            assert shape.intersects(other_shape)
            assert other_shape.intersects(shape)
        # Check when Shapes intersect by one side
        for upper_shape in self.upper_side_intersect_shapes():
            for lower_shape in self.lower_side_intersect_shapes():
                assert lower_shape.intersects(upper_shape)
        # Check when Shapes not intersect
        for shape in inscribed_shapes_list:
            for not_inscribed_shape in (
                self.not_inscribed_rectangle(),
                self.not_inscribed_ellipse(),
                self.not_inscribed_polygon(),
            ):
                assert not shape.intersects(not_inscribed_shape)
                assert not not_inscribed_shape.intersects(shape)

    def test_shape_contains_center(self):
        """
        <b>Description:</b>
        Check Shape contains_center method for Rectangle, Ellipse and Polygon objects

        <b>Expected results:</b>
        Test passes if contains_center method returns expected values

        <b>Steps</b>
        1. Check contains_center method when a Polygon, Rectangle and Ellipse fall within a Rectangle
        2. Check contains_center method when a Polygon, Rectangle and Ellipse fall outside a Rectangle
        """
        rectangle_full = self.fully_covering_rectangle()
        shapes_inside = [self.polygon(), self.ellipse(), self.rectangle()]

        rectangle_part = self.rectangle()
        shapes_outside = [
            self.not_inscribed_polygon(),
            self.not_inscribed_ellipse(),
            self.not_inscribed_rectangle(),
        ]

        for shape_inside in shapes_inside:
            assert rectangle_full.contains_center(shape_inside)
        for shape_outside in shapes_outside:
            assert not rectangle_part.contains_center(shape_outside)

    def test_validate_coordinates(self):
        """
        <b>Description:</b>
        Check Shape validate_coordinates method for Rectangle, Ellipse and Polygon objects

        <b>Expected results:</b>
        Test passes if validate_coordinates method returns expected values

        <b>Steps</b>
        1. Check validate_coordinates method for Shapes with 0.0<=x,y<=1.0
        2. Check validate_coordinates method for Shapes with x<0.0
        3. Check validate_coordinates method for Shapes with x>1.0
        4. Check validate_coordinates method for Shapes with y<0.0
        5. Check validate_coordinates method for Shapes with y>1.0
        6. Check validate_coordinates method for Shapes with x,y<0.0
        7. Check validate_coordinates method for Shapes with x,y>1.0
        8. Check validate_coordinates method for Shapes with x>1.0, y<0.0
        9. Check validate_coordinates method for Shapes with x<1.0, y>1.0
        """
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", r".* coordinates")
            for shape in [self.rectangle(), self.ellipse(), self.polygon()]:
                assert shape._validate_coordinates(x=0.0, y=0.0)
                assert shape._validate_coordinates(x=1.0, y=1.0)
                assert shape._validate_coordinates(x=0.2, y=0.3)
                assert not shape._validate_coordinates(x=-0.1, y=0.0)
                assert not shape._validate_coordinates(x=1.1, y=1.0)
                assert not shape._validate_coordinates(x=0.2, y=-0.3)
                assert not shape._validate_coordinates(x=0.2, y=1.3)
                assert not shape._validate_coordinates(x=-0.1, y=-0.2)
                assert not shape._validate_coordinates(x=1.1, y=1.2)
                assert not shape._validate_coordinates(x=1.2, y=-0.3)
                assert not shape._validate_coordinates(x=-1.2, y=1.3)
