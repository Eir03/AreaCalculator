import math

class AreaCalculator:
    def calculate_area(self, *args):
        if len(args) == 1:
            return self.calculate_circle_area(*args)
        elif len(args) == 3:
            return self.calculate_triangle_area(*args)
        else:
            raise ValueError("Неправильное количество аргументов")
    @staticmethod
    def calculate_circle_area(radius: float) -> float:
        """
        Рассчитывает площадь круга по его радиусу
        """
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        
        area = math.pi * radius ** 2
        return area
    @staticmethod
    def calculate_triangle_area(a: float, b:float, c:float) -> float:
        """
        Рассчитывает площадь треугольника по трем его сторонам
        """
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("С такими сторонами треугольника не существует")
        
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        return area
    
    def is_right_triangle(a: float, b:float, c:float) -> bool:
        sides = [a, b, c]
        sides.sort()

        return sides[0]**2 + sides[1]**2 == sides[2]**2