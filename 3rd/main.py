import tkinter as tk
from tkinter import messagebox
from shapes import PointShape
from shapes import LineShape
from shapes import RectangleShape
from shapes import EllipseShape


# UPd list dict

TOOLS = [
    ("Dot", "Крапка"),
    ("Line", "Лінія"),
    ("Rectangle", "Прямокутник"),
    ("Ellipse", "Еліпс"),
]

SHAPE_CLASSES = {
    "Line": LineShape,
    "Rectangle": RectangleShape,
    "Ellipse": EllipseShape,
}

# UPDATRE


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip = None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)

    def show(self, event):
        self.tip = tk.Toplevel(self.widget)
        self.tip.wm_overrideredirect(True)
        self.tip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        tk.Label(self.tip, text=self.text, bg="lightyellow",
                 relief=tk.SOLID, bd=1).pack()

    def hide(self, event):
        if self.tip:
            self.tip.destroy()
            self.tip = None


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

        self.init_toolbar()

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.on_tool_changed()

    def init_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='Exit', command=self.quit)
        menubar.add_cascade(label='File', menu=file_menu)

        objects_menu = tk.Menu(menubar, tearoff=0)

        for value, name in TOOLS:
            objects_menu.add_radiobutton(
                label=name,
                variable=self.current_tool,
                value=value,
                command=self.on_tool_changed
            )
        menubar.add_cascade(label='Objects', menu=objects_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

# UP тулки

    def init_toolbar(self):
        toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        for value, name in TOOLS:
            btn = tk.Radiobutton(
                toolbar,
                text=name,
                variable=self.current_tool,
                value=value,
                indicatoron=False,
                padx=8,
                command=self.on_tool_changed
            )
            btn.pack(side=tk.LEFT, padx=2, pady=2)
            Tooltip(btn, name)

# ВИніс

    def delete_rubber(self):
        if self.current_rubber_shape:
            self.canvas.delete(self.current_rubber_shape)
            self.current_rubber_shape = None

    def on_tool_changed(self):
        name = dict(TOOLS)[self.current_tool.get()]
        self.title(f"Lab3 - {name}")

    def show_about(self):
        messagebox.showinfo("Довідка", 'Лабка Намбер 3')

    def add_shape_if_allowed(self, shape):
        if len(self.shapes) < 103:
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

        self.delete_rubber()

        shape_class = SHAPE_CLASSES.get(tool)

        if shape_class:
            temp = shape_class(self.start_x, self.start_y, event.x, event.y)
            self.current_rubber_shape = temp.show(self.canvas, rubber=True)

    def on_release(self, event):
        tool = self.current_tool.get()

        if self.start_x == None:
            return

        shape = None

        shape_class = SHAPE_CLASSES.get(tool)
        if shape_class:
            shape = shape_class(self.start_x, self.start_y, event.x, event.y)

        self.delete_rubber()

        if shape:
            self.add_shape_if_allowed(shape)

        self.start_x = None
        self.start_y = None


if __name__ == "__main__":
    app = PaintApp()
    app.mainloop()
