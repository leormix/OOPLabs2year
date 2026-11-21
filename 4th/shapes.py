from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @abstractmethod
    def show(self, canvas, rubber=False):
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
            fill="green", outline="black"
        )


class LineShape(Shape):
    def show(self, canvas, rubber=False, color="black"):
        if rubber:
            return canvas.create_line(
                self.x1, self.y1, self.x2, self.y2,
                fill=color, dash=(4, 4)
            )
        return canvas.create_line(
            self.x1, self.y1, self.x2, self.y2,
            fill=color
        )


class RectangleShape(Shape):

    def show(self, canvas, rubber=False, outline="black", fill="green"):
        left, right = sorted((self.x1, self.x2))
        top, bottom = sorted((self.y1, self.y2))

        if rubber:
            return canvas.create_rectangle(
                left, top, right, bottom,
                outline=outline, fill="", dash=(4, 4)
            )

        return canvas.create_rectangle(
            left, top, right, bottom,
            outline=outline, fill=fill
        )


class EllipseShape(Shape):
    def show(self, canvas, rubber=False, outline="black", fill="deepskyblue"):
        coords = (self.x1, self.y1, self.x2, self.y2)

        if rubber:
            return canvas.create_oval(
                *coords, outline=outline, fill="", dash=(4, 4)
            )
        return canvas.create_oval(
            *coords, outline=outline, fill=fill
        )

# update new figuri


class LineWithCircles(LineShape, EllipseShape):
    def show(self, canvas, rubber=False):
        result = []
        result.append(
            LineShape.show(self, canvas, rubber=rubber, color="darkgreen")
        )

        r = 4
        points = [
            (self.x1, self.y1),
            ((self.x1 + self.x2) // 2, (self.y1 + self.y2) // 2),
            (self.x2, self.y2),
        ]
        for cx, cy in points:
            circle = EllipseShape(cx - r, cy - r, cx + r, cy + r)
            result.append(
                circle.show(
                    canvas,
                    rubber=rubber,
                    outline="darkgreen",
                    fill="gold"
                )
            )
        return result


class CubeFrame(RectangleShape, LineShape):

    def show(self, canvas, rubber=False):
        result = []

        left, right = sorted((self.x1, self.x2))
        top, bottom = sorted((self.y1, self.y2))

        dx = max(8, (right - left) // 4)
        dy = max(8, (bottom - top) // 4)

        back_left = left + dx
        back_right = right + dx
        back_top = top - dy
        back_bottom = bottom - dy

        # Back
        result.append(
            RectangleShape(back_left, back_top, back_right, back_bottom).show(
                canvas, rubber=rubber, outline="navy", fill=""
            )
        )

        # Rebro
        edges = [
            (left, top, back_left, back_top),
            (right, top, back_right, back_top),
            (right, bottom, back_right, back_bottom),
            (left, bottom, back_left, back_bottom),
        ]
        for fx, fy, bx, by in edges:
            result.append(
                LineShape(fx, fy, bx, by).show(
                    canvas, rubber=rubber, color="navy"
                )
            )

        # Front
        result.append(
            RectangleShape(left, top, right, bottom).show(
                canvas, rubber=rubber, outline="navy", fill=""
            )
        )

        return result
