class Circle:
    def area(self):
        return 3.14 * 5 * 5


class Rectangle:
    def area(self):
        return 10 * 5


def show_area(shape):
    print("Area:", shape.area())


circle = Circle()
rectangle = Rectangle()

show_area(circle)
show_area(rectangle)