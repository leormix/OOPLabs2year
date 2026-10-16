from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    @abstractmethod
    def show(self, canvas):
        pass


class PointShape(Shape):
    def __init__(self, x1, y1):
        super().__init__(x1, y1, x1, y1)

    def show(self, canvas):
        r = 2
        return canvas.create_oval(
            self.x1 - r, self.y1 - r, self.x1 + r, self.y1 + r,
            fill="black", outline="black"
        )


class LineShape(Shape):
    def show(self, canvas):
        return canvas.create_line(
            self.x1, self.y1, self.x2, self.y2,
            fill="black",
        )
