import math


# A geometry class that contains x and y values and a translation method for movement
class geometry_shapes():
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y 
    
    @property #a getter property for x
    def getX (self) -> float:
        return self.x

    @getX.setter  #a setter property for x
    def setX(self, x:float) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError (f"X must be a float, not a {type(x)}.")
        if x <= 0:
            raise TypeError(f"X must be > 0.")
        self.x = x
        return self.x

    @property
    def getY (self) -> float:
        return self.y

    @getY.setter
    def setY(self, y:float) -> None:
        if not isinstance(y, (int, float)):
            raise TypeError (f"Y must be a float, not a {type(y)}.")
        if y <= 0:
            raise TypeError(f"Y must be > 0.")
        self.y = y
        return self.y

    #Takes in new values of x and y to move the geometric shape to that position
    def translate(self, new_x:float, new_y:float) -> None:
        if not isinstance(new_x,(int,float)) or not isinstance(new_y, (int,float)):
            raise ValueError("Only values of x and y which are an int or a float")
        if new_x <= 0 or new_y <= 0:
            raise ValueError("Values have to be greater than 0")
        self.x = new_x
        self.y = new_y
    
     # Representation
    def __repr__(self) -> str:
        return f"The geometric shape has its center at ({self.x},{self.y})"

class Circle(geometry_shapes):
    def __init__(self, x: float, y: float, radius:float) -> None:
        super().__init__(x, y) 
        self.radius = radius

    @property #getter method
    def getRadius(self) -> float:
        return self.radius

    @getRadius.setter #setter method
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

    #method to check if the points lie inside of the circle
    def inside_circle(self, xcor, ycor) -> bool:
        if ((self.x-xcor)**2 + (self.y - ycor) **2) - self.radius < 0:
            return True
        else:
            return False
     # Representation
    def __repr__(self) -> str:
        return super().__repr__() + f"  with a radius: {self.radius}"

class Rectangle(geometry_shapes):
    def __init__(self, x: float, y: float, length:float, width:float) -> None:
        super().__init__(x, y)
        self.length = length
        self.width = width 

    @property #a getter method for width
    def getWidth(self) -> float:
        return self.width

    #a setter method for width
    def setWidth(self, width) -> None:
        if not isinstance(width, (int, float)):
            raise TypeError (f"The width must be a float, not a {type(width)}.")
        if width <= 0:
            raise TypeError(f"The width must be greater than  0.")
        self.width = width
        return self.width

    @property #a getter method for length
    def getLength(self) -> float:
        return self.length

    @getLength.setter #setter method for length
    def setLength(self, length) -> None:
        if not isinstance(length, (int, float)):
            raise TypeError (f"The length must be a float, not a {type(length)}.")
        if length <= 0:
            raise TypeError(f"The length must be greater than  0.")
        self.length = length
        return self.length

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return 2 * (self.width + self.length)

    #to check if the points lie inside the rectangle
    def inside_rectangle(self, xcord, ycord) -> bool:
        x2, y2 = self.x+self.length, self.y+self.width
        if (self.x < xcord and xcord < x2):
            if (self.y < ycord and ycord < y2):
                return True
        return False

    def __eq__(self, other) -> bool:
        '''Returns true if two rectangles are the same.'''
        return (type(other) == Rectangle and self.length == other.length and self.width == other.width)

     # Representation
    def __repr__(self) -> str:
        return super().__repr__() + f" with a length: {self.length}, a width of: {self.width}"


class Cube(Rectangle):
    def __init__(self, x: float, y: float, z: float, length: float, width: float, height:float) -> None:
        super().__init__(x, y, length, width)
        self.height = height
        self.z = z

    @property 
    def getHeight(self) -> float:
        return self.height

    @getHeight.setter
    def setHeight(self, height) -> None:
        if not isinstance(height, (int, float)):
            raise TypeError (f"The width must be a float, not a {type(height)}.")
        if height <= 0:
            raise TypeError(f"The width must be greater than  0.")
        self.height = height
        return self.height

    @property
    def getZ (self) -> float:
        return self.z

    @getZ.setter
    def setZ(self, z:float) -> None:
        if not isinstance(z, (int, float)):
            raise TypeError (f"Z must be a float, not a {type(z)}.")
        if z <= 0:
            raise TypeError(f"Z must be > 0.")
        self.z = z
        return self.z

    def surface_area(self):  
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def volume(self):  
        return self.length * self.width * self.height

    #checks if the points lie in the cube
    def inside_cube(self, xcord, ycord, zcord) -> bool:
        x2, y2, z2 = self.x+self.length, self.y+self.width, self.z+self.height
        if (self.x < xcord and xcord < x2 ):
            if (self.y < ycord and ycord < y2 ):
                if (self.z < zcord and zcord <z2 ):
                    return True
        return False

    def translate(self, new_x: float, new_y: float, new_z:float) -> None:
        if not isinstance(new_x,(int,float)) or not isinstance(new_y, (int,float)) or not isinstance(new_z, (int,float)) :
            raise ValueError("Only values of x and y which are an int or a float")
        if new_x <=0 or new_y <=0 or new_z <= 0:
            raise ValueError("Values of x y and z have to be greater than 0")
        self.x = new_x
        self.y = new_y
        self.z = new_z
    
    def __eq__(self, other) -> bool:
        '''Returns true if two cubes are the same.'''
        return (type(other) == Cube and self.length == other.length and self.width == other.width and self.height == other.height)

    # Representation
    def __repr__(self) -> str:
        return super().__repr__() + f" and a height of: {self.height} "

class Sphere(Circle):
    def __init__(self, x: float, y: float, z: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.z = z

    @property
    def getZ (self) -> float:
        return self.z

    @getZ.setter
    def setZ(self, z:float) -> None:
        if not isinstance(z, (int, float)):
            raise TypeError (f"Z must be a float, not a {type(z)}.")
        if z <= 0:
            raise TypeError(f"Z must be > 0.")
        self.z = z
        return self.z
    
    def surfaceArea(self):
        r = self.radius
        self.area = 4 * math.pi * (r * r)
        return self.area

    def volume(self):
        r = self.radius
        self.volume = (4/3) * math.pi * (r * r * r)
        return self.volume

    def inside_sphere(self, xcord, ycord, zcord) -> bool:
        if ((self.x-xcord)**2 + (self.y - ycord) **2) + (self.z - zcord) - self.radius < 0:
            return True
        else:
            return False

    def translate(self, new_x: float, new_y: float, new_z:float) -> None:
        if not isinstance(new_x,(int,float)) or not isinstance(new_y, (int,float)) or not isinstance(new_z, (int,float)) :
            raise ValueError("Only values of x and y which are an int or a float")
        if new_x <=0 or new_y <=0 or new_z <= 0:
            raise ValueError("Values of x y and z have to be greater than 0")
        self.x = new_x
        self.y = new_y
        self.z = new_z
    
    def __eq__(self, other) -> bool:
        '''Returns true if two spheres are the same.'''
        return (type(other) == Sphere and self.radius == other.radius)
    
     # Representation
    def __repr__(self) -> str:
        return super().__repr__()