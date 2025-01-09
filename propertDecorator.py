class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} cm"
    
    @property
    def height(self):
        return f"{self._height:.1f} cm"
    
    @width.setter
    def width(self, new_width):
        if new_width < 0:
            print("width can not be in negative")
        else:
            self._width = new_width

    @height.setter
    def height(self, new_height):
        if new_height < 0:
            print("height can not be in negative")
        else:
            self._height = new_height

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

area = Rectangle(5,6)

area.width = 10
area.height = 20

#del area.width for deletion of width
#del area.height for deletion of height

print(area.height)
print(area.width)
