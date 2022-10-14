import sys, os
import unittest




os.chdir(os.path.dirname(__file__))
path_to_shapes_module = os.path.abspath("../")

sys.path.append(path_to_shapes_module)
print(path_to_shapes_module)

import math
from geometricShapes import geometry_shapes
from geometricShapes import Circle
from geometricShapes import Rectangle

class TestGeometricShape (unittest.TestCase):
    def setUp(self):
        self.x, self.y = 0, 0
     # can be used to create default geometry shapes for testing
    def create_geometric_shape(self) -> geometry_shapes:
        return geometry_shapes(self.x, self.y)

    def test_create_geometric_shape(self):
        """Testing x and y property"""
        #g = geometry_shape(, 2)
        g = self.create_geometric_shape()
        self.assertEqual((g.getX, self.x), (g.getY, self.y))

    def test_translate(self):
        g_shape = self.create_geometric_shape()
        g_shape.translate(5,5)
        self.assertEqual((g_shape.getX, g_shape.getY), (5,5))
    
class TestCircle (unittest.TestCase):
    def setUp(self):
        self.x, self.y, self.radius = 0, 0, 1

    def create_circle(self) -> Circle:
        return Circle(self.x, self.y, self.radius)

    def test_created_circle(self):
        """Testing x,y and radiusproperty"""
        #g = geometry_shape(, 2)
        c = self.create_circle()
        self.assertEqual((c.getX, self.x), (c.getY, self.y), (c.getRadius, self.radius))

    def test_area(self):
        c = self.create_circle()
        self.assertEqual(c.getArea(), math.pi*(self.radius)**2)

    def test_perimeter(self):
        c = self.create_circle()
        self.assertEqual(c.getPerimeter(), 2 * (self.radius) * math.pi)

    def test__eq__(self):
        c1 = Circle(0,0,1)
        c2 = Circle(1,1,1)
        c3 = Circle(0,0,2)
        self.assertEqual(c1==c2, True)
        self.assertEqual(c1==c3, False)

    def test_is_inside(self):
        c = Circle(0,0,1)
        self.assertEqual(c.inside_circle(0.5,0.5), True)
        self.assertEqual(c.inside_circle(10,-1), False)

    def test_translate(self):
        c_shape = self.create_circle()
        c_shape.translate(5,5)
        self.assertEqual((c_shape.getX, c_shape.getY), (5,5))


class TestRectangle (unittest.TestCase):
    def setUp(self):
        self.x, self.y, self.length, self.width = 0, 0, 2,2

    def create_Rectangle(self) -> Rectangle:
        return Rectangle(self.x, self.y, self.length, self.width)

    def test_created_rectangle(self):
        """Testing x,y, width and length property"""
       
        r = self.create_Rectangle()
        self.assertEqual(r.getX, self.x), (r.getY, self.y), (r.getLength, self.length), (r.getWidth, self.width)

    def test_area(self):
        r = self.create_Rectangle()
        self.assertEqual(r.getArea(), (self.length*self.width))

    def test_perimeter(self):
        c = self.create_Rectangle()
        self.assertEqual(c.getPerimeter(), 2 * (self.width + self.length))

    def test__eq__(self):
        r1 = Rectangle(0,0,1,1)
        r2 = Rectangle(1,1,1,1)
        r3 = Rectangle(0,0,2,2)
        self.assertEqual(r1==r2, True)
        self.assertEqual(r1==r3, False)

    def test_is_inside(self):
        r = self.create_Rectangle()
        self.assertEqual(r.inside_rectangle(0.5,0.5), True)
        self.assertEqual(r.inside_rectangle(1,-1), False)

    def test_translate(self):
        r_shape = self.create_Rectangle()
        r_shape.translate(5,5)
        self.assertEqual((r_shape.getX, r_shape.getY), (5,5))



if __name__ == "__main__":
    unittest.main() 