import unittest
import math
from circle import Circle

class TestCircle(unittest.TestCase):
    def test_set_radius_valid(self):
        c = Circle(5.0)
        self.assertAlmostEqual(c.setRadius(0.0), True)
        self.assertAlmostEqual(c.mRadius, 0.0)

    def test_set_radius_invalid(self):
        c = Circle(5.0)
        self.assertAlmostEqual(c.setRadius(-5.0), False)
        self.assertAlmostEqual(c.mRadius, 5.0)
    
    def test_get_radius(self):
        c = Circle(5.0)
        c.mRadius = 25.5
        self.assertAlmostEqual(c.getRadius(), 25.5)
    
    def test_get_area(self):
        c = Circle(2.0)
        self.assertAlmostEqual(c.getArea(), 0)
        c = Circle(1.0)
        self.assertAlmostEqual(c.getArea(), math.pi)
        c = Circle(4.0)
        self.assertAlmostEqual(c.getArea(), math.pi * 16.0)

    def test_ctor(self):
        c = Circle(20.0)
        self.assertAlmostEqual(c.mRadius, 20.0)

    def test_ctor_invalid(self):
        # The circle should NOT allow a radius below 0.
        c = Circle(-5.0)
        self.assertNotAlmostEqual(c.mRadius, -5.0)
    
    def test_get_circumference(self):
        c = Circle(0.5)
        self.assertAlmostEqual(c.getCircumference(), math.pi)

    