import tkinter as tk
from tkinter import messagebox
from shapes import PointShape
from shapes import LineShape
from shapes import RectangleShape
from shapes import EllipseShape


class PaintApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main window")
        self.geometry("500x400")

        self.current_tool = tk.StringVar(value="Dot")
        self.shapes = []

        self.start_x = None
        self.start_y = None
        self.current_rubber_shape = None

        self.init_menu()

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def init_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='Exit', command=self.quit)
        menubar.add_cascade(label='File', menu=file_menu)

        objects_menu = tk.Menu(menubar, tearoff=0)

        tools = ["Dot", "Line", "Rectangle", "Ellipse"]

        for tool in tools:
            objects_menu.add_radiobutton(
                label=tool,
                variable=self.current_tool,
                value=tool,
                command=self.on_tool_changed
            )
        menubar.add_cascade(label='Objects', menu=objects_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

    def on_tool_changed(self):
        print(f"Chosen instrument: {self.current_tool.get()}")

    def show_about(self):
        messagebox.showinfo("Help", 'Some info')

    def add_shape_if_allowed(self, shape):
        if len(self.shapes) < 102:
            self.shapes.append(shape)
            shape.show(self.canvas)

    def on_press(self, event):
        tool = self.current_tool.get()
        if tool == "Dot":
            shape = PointShape(event.x, event.y)
            self.add_shape_if_allowed(shape)
        elif tool in ("Line", "Rectangle", "Ellipse"):
            self.start_x = event.x
            self.start_y = event.y

    def on_motion(self, event):
        tool = self.current_tool.get()
        if self.start_x is None:
            return

        if self.current_rubber_shape:
            self.canvas.delete(self.current_rubber_shape)
            self.current_rubber_shape = None

        if tool == "Line":
            self.current_rubber_shape = self.canvas.create_line(
                self.start_x, self.start_y, event.x, event.y,
                fill="blue"
            )
        elif tool == "Rectangle":
            self.current_rubber_shape = self.canvas.create_rectangle(
                self.start_x, self.start_y, event.x, event.y,
                outline="blue", fill=""
            )
        elif tool == "Ellipse":
            rx = (event.x - self.start_x)
            ry = (event.y - self.start_y)
            self.current_rubber_shape = self.canvas.create_oval(
                self.start_x - rx, self.start_y - ry,
                self.start_x + rx, self.start_y + ry,
                outline="blue", fill=""
            )

    def on_release(self, event):
        tool = self.current_tool.get()

        if self.start_x == None:
            return

        shape = None

        if tool == "Line":
            shape = LineShape(self.start_x, self.start_y, event.x, event.y)
        elif tool == "Rectangle":
            shape = RectangleShape(
                self.start_x, self.start_y, event.x, event.y)
        elif tool == "Ellipse":
            shape = EllipseShape(self.start_x, self.start_y, event.x, event.y)

        if self.current_rubber_shape:
            self.canvas.delete(self.current_rubber_shape)
            self.current_rubber_shape = None

        if shape:
            self.add_shape_if_allowed(shape)

        self.start_x = None
        self.start_y = None


if __name__ == "__main__":
    app = PaintApp()
    app.mainloop()
