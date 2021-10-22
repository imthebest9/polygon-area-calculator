class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        pic = ""
        for row in range(self.height):
            for col in range(self.width):
                pic += "*"
            pic += '\n'
        
        return pic
    
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __repr__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        self.side = side

    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side

    def __repr__(self):
        return 'Square(side={})'.format(self.side)
    
    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height

