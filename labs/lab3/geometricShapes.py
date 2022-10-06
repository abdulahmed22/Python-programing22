import math

class geometry_shapes():
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y 
    def getX (self) -> float:
        return self.x

    def setX(self, x:float) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError (f"X must be a float, not a {type(x)}.")
        if x <= 0:
            raise TypeError(f"X must be > 0.")
        self.x = x
        return self.x

    def getY (self) -> float:
        return self.y

    def setY(self, y:float) -> None:
        if not isinstance(y, (int, float)):
            raise TypeError (f"Y must be a float, not a {type(y)}.")
        if y <= 0:
            raise TypeError(f"Y must be > 0.")
        self.y = y
        return self.y

    def translate(self, new_x:float, new_y:float) -> None:
        self.x = new_x
        self.y = new_y

class Circle(geometry_shapes):
    def __init__(self, x: float, y: float, radius:float) -> None:
        super().__init__(x, y) 
        self.radius = radius

    def getRadius(self) -> float:
        return self.radius

    def setRadius(self, radius:float) -> None:
        if not isinstance(radius, (int, float)):
            raise TypeError (f"The radius must be a float, not a {type(radius)}.")
        if radius <= 0:
            raise TypeError(f"The radius must be > 0.")
        self.radius = radius
        return self.radius

    def getArea(self):
        return (self.radius **2) * math.pi
  
    def getDiameter(self):
        return 2 * self.radius
  
    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def __eq__(self, other) -> bool:
        '''Returns true if two circles are the same.'''
        return (type(other) == Circle and self.radius == other.radius)

    def inside_circle(self, xcor, ycor) -> bool:
        if ((self.x-xcor)**2 + (self.y - ycor) **2) - self.radius < 0:
            return True
        else:
            return False


class Rectangle(geometry_shapes):
    def __init__(self, x: float, y: float, length:float, width:float) -> None:
        super().__init__(x, y)
        self.length = length
        self.width = width 

    def getWidth(self) -> float:
        return self.width

    def setWidth(self, width) -> None:
        self.width = width

    def getLength(self) -> float:
        return self.length

    def setLength(self, length) -> None:
        self.length = length

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return 2 * (self.width + self.length)

    def __eq__(self, other) -> bool:
        '''Returns true if two rectangles are the same.'''
        return (type(other) == Rectangle and self.length == other.length and self.width == other.width)

class Sphere(Circle):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)