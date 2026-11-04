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

    @staticmethod
    def _rubber_style():
        return {"outline": "black", "fill": "", "dash": (4, 4)}


class PointShape(Shape):
    def __init__(self, x1, y1):
        super().__init__(x1, y1, x1, y1)

    def show(self, canvas, rubber=False):
        r = 2
        return canvas.create_oval(
            self.x1 - r, self.y1 - r, self.x1 + r, self.y1 + r,
            fill="black", outline="black"
        )


class LineShape(Shape):
    def show(self, canvas, rubber=False):
        if rubber:
            return canvas.create_line(
                self.x1, self.y1, self.x2, self.y2,
                fill="black", dash=(4, 4)
            )

        return canvas.create_line(
            self.x1, self.y1, self.x2, self.y2,
            fill="black",
        )


class RectangleShape(Shape):
    def show(self, canvas, rubber=False):
        dx = (self.x1 - self.x2)
        dy = (self.y1 - self.y2)

        if rubber:
            return canvas.create_rectangle(self.x1 - dx, self.y1 - dy, self.x1 + dx, self.y1 + dy,
                                           **self._rubber_style())

        return canvas.create_rectangle(
            self.x1 - dx, self.y1 - dy, self.x1 + dx, self.y1 + dy,
            outline='black', fill=''
        )


class EllipseShape(Shape):

    def show(self, canvas, rubber=False):
        coords = (self.x1, self.y1, self.x2, self.y2)

        if rubber:
            return canvas.create_oval(self.x1, self.y1, self.x2, self.y2, **self._rubber_style())
        return canvas.create_oval(
            *coords, outline="black", fill="deepskyblue"
        )
