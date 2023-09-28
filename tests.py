import math
import unittest
from area_calculator import AreaCalculator

class TestAreaCalculator(unittest.TestCase):
    def test_circle_area(self):
        radius = 5.0
        expected_area = math.pi * radius ** 2
        self.assertEqual(AreaCalculator.calculate_circle_area(radius), expected_area)

    def test_triangle_area(self):
        a, b, c = 5.0, 7.0, 8.0

        # Формула Герона
        expected_area = math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
        self.assertAlmostEqual(AreaCalculator.calculate_triangle_area(a, b, c), expected_area, places=2)

    def test_right_triangle(self):
        a, b, c = 3.0, 4.0, 5.0
        self.assertTrue(AreaCalculator.is_right_triangle(a, b, c))

        a, b, c = 5.0, 7.0, 8.0
        self.assertFalse(AreaCalculator.is_right_triangle(a, b, c))

if __name__ == '__main__':
    unittest.main()